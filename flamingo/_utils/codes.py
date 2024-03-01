import random
import math

from _config.config import config
from _config.departments import departments
from _config.objects import characters
from .strings import reverse_str

def create_item_code(cost = 0, code = departments.Art):
	cost = math.ceil(cost)
	return (reverse_str(str(cost)) + code[0].upper() + create_char_code(length= 7 - len(str(cost)), alpha= 'upper')).upper()

def create_char_code(length = config['code_length'], alpha = 'all'):
	output: string = ''
	chars: [] = [] + characters['num']
	if alpha != 'num':
		if alpha == 'upper':
			chars += [x.upper() for x in characters['alpha']]
		elif alpha == 'lower':
			chars += characters['alpha']
		else:
			chars += characters['alpha'] + [x.upper() for x in characters['alpha']]
	for x in [''] * length:
		randomNumber = int(random.random() * len(chars))
		output = str(output) + str(chars[randomNumber])
	return output