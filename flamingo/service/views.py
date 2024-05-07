from django.shortcuts import render

def home(request):
	return render(request, 'service/service-home.html', {})

def hauling(req):
	return render(req, 'service/service-pools.html', {})

def assembly(req):
	return render(req, 'service/service-assembly.html', {})

def pools(req):
	return render(req, 'service/service-pools.html', {})

def cleanup(req):
	return render(req, 'service/service-pools.html', {})

def etc(req):
	return render(req, 'service/service-pools.html', {})