window.addEventListener('DOMContentLoaded', () => {
	useNumberOnlyInput()
	useMoneyValueInput()
})

function useNumberOnlyInput() {
	// get all elements with the 'number-input' class and escape if none found
	const query = document.getElementsByClassName('number-input')
	if (!query.length) return
	// loop over results to apply the listener
	Array.from(query).forEach(q => {
		const defaultValue = q.value
		q.addEventListener('keypress', (e) => {
			// ignore any non digits
			if (!e.key.match(/^[0-9]/)) e.preventDefault()
		})
		q.addEventListener('blur', (e) => {
			// reset default value
			if (!q.value) q.value = defaultValue
		})
	})
}

function useMoneyValueInput() {
	// get all elements with the 'money-input' class and escape if none found
	const query = document.getElementsByClassName('money-input')
	if (!query.length) return
	// loop over results to apply the listener
	Array.from(query).forEach(q => {
		q.addEventListener('keypress', (e) => {
			// ignore any non digits
			if (!e.key.match(/^[0-9.]/)) e.preventDefault()
			// allow only 1 decimal point
			if (/\./.test(q.value) && e.key === '.') e.preventDefault()
		})
		q.addEventListener('blur', (e) => {
			// round up to the nearest penny
			q.value = currencyDisplay(q.value)
		})
	})
}

function currencyDisplay(value = '0') {
	const splitValue = String(value).split('.')
	if (splitValue.length <= 1) return value + '.00'
	// handle multiple decimal points with warning and ignoring all except first
	if (splitValue.length > 2) {
		console.warn('Multiple decimals entered. Only the first one will be used for calculation.')
		splitValue[1] = splitValue.slice(1).join('')
	}
	// throw error if the decimal portion contains non-digits
	if (Number(splitValue[1]) * 0 !== 0) throw new Error('Invalid value. Cannot round a non-digit.')
	// add additional placeholder values that will be used for rounding formula
	splitValue[1] += '000'
	return [splitValue[0], Math.ceil(Number(splitValue[1].slice(0, 3)) / 10)].join('.')
}