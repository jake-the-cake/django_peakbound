def reverse_str(value = None):
	if not value: return ''
	split_value = [ x for x in str(value) ]
	output_chars = []
	for v in split_value:	output_chars = [ str(v) ] + output_chars
	return ''.join(output_chars)