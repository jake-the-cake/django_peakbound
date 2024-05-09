from django.shortcuts import render
from _data.services import pages

def home(request):
	return render(request, 'service/service-home.html', {
		'pages': [
			pages['pools'],
			pages['assembly'],
			pages['hauling'],
			pages['cleanup'],
			pages['etc']
		]
	})

def hauling(req):
	return render(req, 'service/service-details.html', {
		'details': pages['hauling']
	})

def assembly(req):
	return render(req, 'service/service-details.html', {
		'details': pages['assembly']
	})

def pools(req):
	return render(req, 'service/service-details.html', {
		'details': pages['pools']
	})

def cleanup(req):
	return render(req, 'service/service-details.html', {
		'details': pages['cleanup']
	})

def etc(req):
	return render(req, 'service/service-details.html', {
		'details': pages['etc']
	})