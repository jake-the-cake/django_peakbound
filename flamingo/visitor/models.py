from django.db import models
from _utils.codes import createCharacterCode

class Visitor(models.Model):
	
	userCode = models.CharField(
		max_length = 16,
		default = createCharacterCode()
	)
	
	ip = models.CharField(
		max_length = 15,
		default = '000.000.000.000'
	)
	
	created = models.DateTimeField(
		auto_now_add = True
	)
	
	# account = models.ForeignKey(
	# 	'User',
	# 	on_delete = models.PROTECT,
	# 	null = True,
	# 	default = None
	# )
	
	visits = models.IntegerField(
		default = 1
	)
	
	def __str__(self):
		return self.userCode