function useExpandingContactForm(options = {}) {
  if (!Array.isArray(options.serviceValue)) options.serviceValue = new Array(options.serviceValue)

  const buttons = document.querySelectorAll('#contact-btn')
  if (buttons && buttons.length > 0) {
    buttons.forEach((btn, idx) => {
      // GET BUTTON
      if (btn) {
        // HIDE CLOSE LINK
        const close = btn.querySelector('#contact-close') || document.createElement('span')
        if (!close.innerText) {
          close.innerText = 'x'
          close.id = 'contact-close'
          close.classList.add('accent-bubble-sm')
          btn.appendChild(close)
        }
        close.classList.toggle('d-none')
        // FORM
        const form = btn.parentNode.querySelector('form')
        if (!form) return false
        form.id = 'contact-form-' + idx
        if (options.serviceValue) form.querySelector('select').value = options.serviceValue[idx]
        form.onsubmit = Handlers.contactFormSubmit(form.id)
        // BUTTON ONCLICK EVENT
        btn.onclick = (e) => {
          close.classList.toggle('d-none')
          btn.classList.toggle('form-header-exp')
          form.classList.toggle('h-0')
        }
      }
    })
  }
}