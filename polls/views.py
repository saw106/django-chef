from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return HttpResponse("Hello, you have arrived at the polls landing page.")

def chef_test(request):
	return HttpResponse('43frOIJtjq90324jwoierfm')

