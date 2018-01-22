from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
	context_dict = {'boldmessage': "this is bold, man!"}
	return render(request, 'rango/index.html', context=context_dict)
	
def about(request):
	context_dict = {'boldmessage': "don't forget to rock on!"}
	return render(request, 'rango/about.html', context=context_dict)