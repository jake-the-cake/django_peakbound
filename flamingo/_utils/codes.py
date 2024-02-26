import random
import math

from _config.config import config
from _config.objects import characters

def createCharacterCode(length = 16, alpha = 'all', **args):
	outputString = ''
	chars = characters['num']
	print('x' ,chars)
	if alpha == 'all':
		chars += characters['alpha'] + [x.upper() for x in characters['alpha']]
	elif alpha == 'upper':
		chars += [x.upper() for x in characters['alpha']]
	elif alpha == 'lower':
		chars += characters['alpha']
	print('y', chars)
	for x in [''] * length:
		randomNumber = int(random.random() * len(chars))
		outputString = str(outputString) + str(chars[randomNumber])
	return outputString

def create_item_code(cost, code):
	cost = math.ceil(cost)
	return (str(cost) + code.upper() + createCharacterCode(length= 7 - len(str(cost)), alpha= 'upper')).upper()

	def create_char_code(length = config.code_length, alpha = 'all'):
		print(length, alpha)