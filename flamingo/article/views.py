from django.shortcuts import render

# Create your views here.
def view_all(request):
	return render(request, 'article/view-all.html', { 'text': 'test'})