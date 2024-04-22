# from django.http import HttpResponse
from django.shortcuts import render
from _config.links import footer

def homepage(request):
	return render(request, 'home.html', { 'site': 'peakbound', 'links': footer['peakbound']})


def about(request):
	return render(request, 'about.html')