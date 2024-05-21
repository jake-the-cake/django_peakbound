class Qform {
  constructor( id ) {
    this.form = document.getElementById(id) || null
    if (!this.form) return null
    this.id = String(id)
    this.error = false
    this.errorResponse = null
    this.getFormElements()
  }

  getFormElements() {
    const inputs = this.form.querySelectorAll('input')
    const textareas = this.form.querySelectorAll('textarea')
    const selects = this.form.querySelectorAll('select')
    this.buttons = this.form.querySelectorAll('button')
    this.fields = []
    this.elements = [
      ...inputs,
      ...selects,
      ...textareas
    ]
    this.elements.forEach(( element, index ) => {
      this.fields[index] = element.name
    })
  }

  resetErrors() {
    this.form.querySelectorAll('.form-error').forEach( element => element.parentNode.removeChild(element))
  }

  useValidation( tests ) {
    this.resetErrors()
    this.error = false
    Object.entries(tests).forEach( t => {
      tests[t[0]].forEach(field => {
        const { errorResponse } = this.validate(field, t[0])
        if (errorResponse){
          this.error = true
          const span = document.createElement('span')
          const label = this.getElementLabel(field)
          span.innerText = errorResponse.message || 'error'
          span.classList.add('form-error', 'ms-2')
          label.appendChild(span)
          this.errorResponse = null
        }
      })
    })
  }

  validate( field, validation ) {
    switch( validation ) {
      case 'required': return this.isRequired(field)
      case 'unique': return this.isRequired(field)
      case 'phone': return this.isPhone(field)
      case 'email': return this.isEmail(field)
      default: return
    }
  }

  isRequired( field ) {
    const index = this.fields.indexOf(field)
    if (typeof index !== 'number') return console.warn('warning')
    const element = this.elements[index]
    if (!element) return console.warn(`Field name not found -- (${ field })`)
    if (!element.value) this.errorResponse = new Error(`This field is required -- (${ field })`)
    return this
  }

  isPhone( field ) {
    const element = this.getElementByName(field)
    const regex = /^\(?(\d{3})\)?[- ]?(\d{3})[- ]?(\d{4})$/
    console.log(regex.test(element.value))
    if (!regex.test(element.value)) this.errorResponse = new Error(`Invalid format -- (${ field })`)
    return this
  }

  isEmail( field ) {    
    const element = this.getElementByName(field)
    if (!element) return console.warn(`Field name not found -- (${ field })`)
    const regex = /^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$/
    if (!regex.test(element.value)) this.errorResponse = new Error(`Invalid format -- (${ field })`)
    return this
  }

  getElementByName( name ) {
    return this.elements.filter( element => element.name === name)[0] || null
  }

  getElementLabel( name ) {
    return this.getElementByName(name)?.parentElement?.querySelector('label') ?? null
  }

  sendData() {
    const json = {}
    const formdata = new FormData(this.form)
    Array.from(formdata).forEach(([ key, value ])=> {
      json[key] = value
    })
    return JSON.stringify(json)
  }
}

class Handlers {
  static contactFormSubmit( id ) {
    return ( e ) => {
      e.preventDefault()
      const form = new Qform(id)
      if (!form) return new Error('Form ID not found')
      form.useValidation({
        required: ['name', 'service', 'phone'],
        phone: ['phone'],
        email: ['email'],
        unique: []
      })
      if (form.error === false) {
        fetch('/api/customer/add', {
          method: 'POST',
          body: form.sendData()
        })
      }
    }
  }
}

window.addEventListener('DOMContentLoaded', () => {
  Handlers.contactFormSubmit('contact-form-0')
})
