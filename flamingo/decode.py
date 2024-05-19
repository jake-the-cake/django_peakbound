pyramid = [
	[1],
	[2, 3],
	[4, 5, 6]
]

def decode(message_file):
	numeric_code = []
	with open(message_file, 'r') as file:
		lines = []
		for line in file:
			lines.append(line.strip().split(' '))
		for row in pyramid:
			code_word = [line for line in lines if line[0] == str(row[-1])][0]
			numeric_code.append(code_word[1])
		print( ' '.join(numeric_code))
		return ' '.join(numeric_code)

decode('textfile.txt')