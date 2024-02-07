from rest_framework.response import Response
from rest_framework.decorators import api_view
from shop.models import Item
from django.core import serializers
import json
from _utils.codes import create_item_code

@api_view(['GET'])
def get_items(request):
	item = Item.objects.get()
	return Response(serializers.serialize('json', [item]))

@api_view(['POST'])
def add_item(request):
	body = json.loads(request.body.decode('utf-8'))
	itemCode = create_item_code(1.2, 'a')
	item = Item(
		item_code = itemCode,
		sku = body['sku'] or itemCode,
		item_name = body['item_name'],
		description = body['description'],
		cost = body['cost'] or 0,
		price = body['price'] or 0,
		stock = body['stock'] or 1,
	)
	item.save()
	return Response(serializers.serialize('json', [item]))

@api_view(['POST'])
def edit_item(request):
	body = json.loads(request.body.decode('utf-8'))
	item = Item.objects.get()
	item = Item(
		item_code = body['item_code'],
		item_name = body['item_name'],
		description = body['description'],
		cost = body['cost'],
		price = body['price'],
		stock = body['stock'],
		sku = body['sku'],
	)
	item.save()
	return Response(serializers.serialize('json', [item]))

@api_view(['DELETE'])
def delete_item(request, id):
	item = Item.objects.filter(item_code = id)[0]
	item.delete()
	return Response(serializers.serialize('json', [item]))