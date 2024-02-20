from django.db import models
from datetime import datetime
from visitor.models import User

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
	sku = models.CharField(max_length=24)

class Promo(models.Model):
	code = models.CharField(max_length=12)
	description = models.TextField(default='Discount')
	discount_type = models.CharField(max_length=12, default='percent')
	discount_value = models.IntegerField(default=0)
	applicable_items = models.ManyToManyField(Item)
	can_combine = models.BooleanField(default=False)

class Order(models.Model):
	order_code = models.CharField(max_length=24)
	customer = models.ForeignKey(User, on_delete=models.CASCADE)
	status = models.CharField(max_length=10)
	total = models.FloatField(default=0)
	promos = models.ManyToManyField(Promo)

class OrderLine(models.Model):
	order = models.ForeignKey(Order, on_delete=models.CASCADE)
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
	quantity = models.IntegerField(default=1)
	price = models.FloatField(default=0)
	promo_price = models.FloatField(default=0)
	promo_code = models.CharField(max_length=12)