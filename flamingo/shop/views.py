from django.shortcuts import render
from datetime import datetime, timedelta
from django.core.paginator import Paginator

#
#
#
''' funtions to be put elsewhere '''
def daysElapsed(target_datetime, days_to_check: int) -> bool:
	return timedelta(days = days_to_check) < datetime.now() - target_datetime

def capital_first_lower_rest(string: str) -> str:
	if (type(string) != str): return ''
	return string[0].upper() + string[1:len(string)].lower()

def capital_all_first_lower_rest(string: str) -> str:
	if (type(string) != str): return ''
	wordArray = string.split(' ')
	for i, word in enumerate(wordArray):
		wordArray[i] = capital_first_lower_rest(word)
	return ' '.join(wordArray)
#
#
#
''' dummy data '''
item = { 'name': 'This Item Here', 'price': 5 }
item2 = { 'name': 'This Other Item Here' }
item3 = { 'name': 'Proper Item', 'stock': 5 }
item4 = { 'name': 'Still on the row?', 'price': 8 }
item5 = { 'name': 'New row', 'created': datetime(2024,2,2,0,0) }

items = [ item, item2, item3, item4, item5 ]

for i in items:
	if 'created' in i: i['is_recent'] = not daysElapsed(i['created'], 14)
	if not 'stock' in i: i['stock'] = 'tbd'

#
#
#

def home(request):
	return render(request, 'shop/shop-home.html', { 'items': items[0:3] })

def item_list(request):
	search_by = request.GET.get('searchBy')
	paginator = Paginator(items, 2)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	item_count = {
		'start': (2 * (int(page_number) - 1)) + 1,
		'end': min(2 * int(page_number), len(items)),
		'total': len(items)
	}
	return render(request, 'shop/shop-item-list.html', {
		'page_obj': page_obj,
		'item_count': item_count,
		'searchBy': capital_all_first_lower_rest(search_by)
	 })