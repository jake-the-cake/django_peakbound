# from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
	return render(request, 'home.html', { 'site': 'peakbound' })


def about(request):
	return render(request, 'about.html')