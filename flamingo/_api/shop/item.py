from rest_framework.response import Response
from rest_framework.decorators import api_view
from shop.models import Item
from django.core import serializers
import json

@api_view(['GET'])
def get_items(request):
	item = Item.objects.get()
	return Response(serializers.serialize('json', [item]))

@api_view(['POST'])
def add_item(request):
	body = json.loads(request.body.decode('utf-8'))
	item = Item(
		item_code = body['item_code'],
		item_name = body['item_name'],
		description = body['description'],
		cost = body['cost'],
		price = body['price'],
		stock = body['stock'],
	)
	item.save()
	return Response(serializers.serialize('json', [item]))