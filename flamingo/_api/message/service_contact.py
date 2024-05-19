from rest_framework.response import Response
from rest_framework.decorators import api_view
from visitor.models import Customer
from django.core import serializers
import json
from _utils.codes import create_char_code
from _config.departments import departments

from visitor.models import Customer

def get_body(req):
	return json.loads(req.body.decode('utf-8'))

@api_view(['GET'])
def get_items(request):
	# item = Item.objects.get()
	return Response(serializers.serialize('json', [item]))

@api_view(['POST'])
def new_message( req ):
	body = get_body(req)
	c_code = body['phone'] or create_char_code(10, 'num')
	c = None
	if Customer.objects.count() > 0:
		c = Customer.objects.get(customer_code = c_code)
	if not c:	
		c = Customer(
		customer_code = c_code,
		# name = body['name'],
		# email = body['email'],
		# visitor_ids = []
	)
		print(c)
	# if len(c) < 1: print('not found')
	# c = Customer(
	# 	customer_code = c_code,
	# 	sku = body['sku'] or itemCode,
	# 	item_name = body['item_name'],
	# 	description = body['description'],
	# 	cost = body['cost'] or 0,
	# 	price = body['price'] or 0,
	# 	stock = body['stock'] or 1,
	# )
	# item.save()
	# return Response(serializers.serialize('json', [c]))
	return Response({})