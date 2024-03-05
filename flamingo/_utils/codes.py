import random
import math

from _config.config import config
from _config.departments import departments
from _config.objects import characters
from .strings import reverse_str

def check_item_code(model, code, query):
	# print(kwargs)
	if model and code:
		# kv = None
		# for k,v in kwargs:
		# 	if not kv:
		# 		kv = {
		# 			'key': k,
		# 			'value': v
		# 		}

		if len(model.objects.filter(query)) < 1:
			return False
		else:
			return True
	return False

def create_item_code(cost = 0, code = departments.Art, model = None):
	str_cost = reverse_str(str(math.ceil(cost)))
	char_code = create_char_code(config['item_code_length'] - len(code) - len(str_cost), 'upper')
	item_code = str_cost + code + char_code
	if model and check_item_code(model, item_code, {'item_code': item_code}):
		return create_item_code(cost, code, model)
	else:
		return item_code

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