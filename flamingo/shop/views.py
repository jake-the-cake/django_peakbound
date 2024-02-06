from django.shortcuts import render

def home(request):
	item = { 'name': 'This Item Here' }
	item2 = { 'name': 'This Other Item Here' }
	item3 = { 'name': 'Proper Item' }
	items = [ item, item2, item3 ]
	return render(request, 'shop/shop-home.html', { 'items': items })