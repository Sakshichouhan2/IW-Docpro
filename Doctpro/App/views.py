from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def RegisterView(request):
	return render(request, "App/sign-up.html") 

def  Login(request):
	return render(request, "App/learn-more.html") 
