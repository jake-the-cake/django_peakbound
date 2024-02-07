import random
import math

characters = {
	'num': [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
	'alpha': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
					 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
}

def createCharacterCode(length = 16, alpha = 'all', **args):
	outputString = ''
	chars = characters['num']
	if alpha == 'all':
		chars += characters['alpha'] + [x.upper() for x in characters['alpha']]
	elif alpha == 'upper':
		chars += [x.upper() for x in characters['alpha']]
	elif alpha == 'lower':
		chars += characters['alpha']
	for x in [''] * length:
		randomNumber = int(random.random() * len(chars))
		outputString = str(outputString) + str(chars[randomNumber])
	return outputString

def create_item_code(cost, code):
	cost = math.ceil(cost)
	return (str(cost) + code.upper() + createCharacterCode(length= 7 - len(str(cost)), alpha= 'upper')).upper()