class Qform {
  constructor( id ) {
    this.form = document.getElementById(id) || null
    if (!this.form) return null
    this.id = String(id)
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

  useValidation( tests ) {
    Object.entries(tests).forEach( t => {
      tests[t[0]].forEach(field => {
        const result = this.validate(field, t[0])
      })
    })
  }

  validate( field, validation ) {
    switch( validation ) {
      case 'required': return this.isRequired(field)
      case 'unique': return this.isRequired(field)
      case 'phone': return this.isRequired(field)
      case 'email': return this.isEmail(field)
      default: return
    }
  }

  isRequired( field ) {
    const index = this.fields.indexOf(field)
    if (typeof index !== 'number') return console.warn('warning')
    const element = this.elements[index]
    if (!element) return console.warn(`Field name not found -- (${ field })`)
    if (!element.value) return new Error(`This field is required -- (${ field })`)
  }

  isEmail( field ) {
    const element = this.elements[this.fields.indexOf(field)]
    console.log(field)
    console.log(element)
    console.log(this.fields.indexOf(field))
  }
}

class Handlers {
  static contactFormSubmit( id ) {
    this.form = new Qform(id)
    if (!this.form) return new Error('Form ID not found')
    this.form.useValidation({
      required: ['name', 'service'],
      phone: ['phone'],
      email: ['email'],
      unique: []
    })
    // console.log(this.form)
    // console.log(this.form.isRequired('name'))
  }
}

window.addEventListener('DOMContentLoaded', () => {
  Handlers.contactFormSubmit('contact-form-0')
})
