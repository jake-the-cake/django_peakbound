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
        if (options.serviceValue) form.querySelector('select').value = options.serviceValue[idx]
        form.onsubmit = (e) => {
          e.preventDefault()
          const data = new FormData(e.target)
          console.log(data)
        }
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