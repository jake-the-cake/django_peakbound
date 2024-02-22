from rest_framework.response import Response
from rest_framework.decorators import api_view
from shop.models import Order, OrderLine, Item
from django.core import serializers
import json
from _utils.codes import create_item_code

@api_view(['GET'])
def get_orders(request):
	orders = Order.objects.get()
	return Response(serializers.serialize('json', [orders]))

@api_view(['POST'])
def add_order(request):
	body = json.loads(request.body.decode('utf-8'))
	# itemCode = create_item_code(1.2, 'a')
	order = Order.objects.filter(customer='Customer A', status='cart') or None
	if len(order) > 1: order = order[0]
	if not order:
		order_code = 'codetobemade'
		order = Order(
			order_code = order_code,
			status = 'cart',
			total = 0,
			# promos = Order.promos.set()
		)
		order.save()
	print(order)
	item = Item.objects.get(id=body['id'])
	line = OrderLine(
		order = Order.objects.get(id=order.id),
		item = item,
		# item = Item.objects.get(id=body['id']),
		quantity = body['qty'],
	)
	line.save()
	order.lines.add(line)
	order.save()
	print(line.item)
	return Response(serializers.serialize('json', [order]))

# @api_view(['POST'])
# def edit_order(request):
# 	body = json.loads(request.body.decode('utf-8'))
# 	item = Item.objects.get()
# 	item = Item(
# 		item_code = body['item_code'],
# 		item_name = body['item_name'],
# 		description = body['description'],
# 		cost = body['cost'],
# 		price = body['price'],
# 		stock = body['stock'],
# 		sku = body['sku'],
# 	)
# 	item.save()
# 	return Response(serializers.serialize('json', [item]))

# @api_view(['DELETE'])
# def delete_order(request, id):
# 	item = Item.objects.filter(item_code = id)[0]
# 	item.delete()
# 	return Response(serializers.serialize('json', [item]))