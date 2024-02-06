from django.shortcuts import render
from datetime import datetime, timedelta

def home(request):
	item = { 'name': 'This Item Here', 'price': 5 }
	item2 = { 'name': 'This Other Item Here' }
	item3 = { 'name': 'Proper Item', 'stock': 5 }
	item4 = { 'name': 'Still on the row?', 'price': 8 }
	item5 = { 'name': 'New row', 'created': datetime(2024,2,2,0,0) }
	items = [ item, item2, item3, item4, item5 ]
	for i in items:
		if 'created' in i: i['is_recent'] = not daysElapsed(i['created'], 14)
		if not 'stock' in i: i['stock'] = 'tbd'
	return render(request, 'shop/shop-home.html', { 'items': items })

def daysElapsed(target_datetime, days_to_check: int) -> bool:
	return timedelta(days = days_to_check) < datetime.now() - target_datetime