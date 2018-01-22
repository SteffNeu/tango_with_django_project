from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
	context_dict = {'boldmessage': "this is bold, man!"}
	return render(request, 'rango/index.html', context=context_dict)
	
def about(request):
	return HttpResponse("Rango says here is the about page. <a href='/rango/'>Index</a>")