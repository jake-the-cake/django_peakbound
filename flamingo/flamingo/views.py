# from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
	return render(request, 'layout.html')
	# return HttpResponse('Look at me.')


def about(request):
	return render(request, 'about.html')
	# return HttpResponse('About face!')