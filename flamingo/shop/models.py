from django.db import models
from datetime import datetime

# Create your models here.
class Item(models.Model):
	item_code = models.CharField(max_length=24)
	item_name = models.CharField(max_length=100)
	created_on = models.DateTimeField(default = datetime.now())
	created_by = models.CharField(max_length=100, default='Jason')
	cost = models.FloatField(default=0)
	price = models.FloatField(default=0)
	stock = models.IntegerField(default=1)
	description = models.TextField(default='description', max_length=500)