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
    console.log(this.elements)
    console.log(this.fields)
  }



  validate( field, validation ) {

  }
}

class Handlers {
  static contactFormSubmit( id ) {
    return ( e ) => {
      e.preventDefault()
      this.form = new Qform(id)
      if (!this.form) return new Error('Form ID not found')
      console.log(this.form)
      fetch('/api/customer/add', {
        method: 'POST',
        body: JSON.stringify({"phone": "1234154545"})
      })
    }
  }
}

window.addEventListener('DOMContentLoaded', () => {
  Handlers.contactFormSubmit('contact-form-0')
})
