from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse("hello world")
    return render(request,'webApp/index.html')

def about(request):
    # return HttpResponse("Hello from About page")
     return render(request,'webApp/about.html')

def contact(request):
    return HttpResponse("Hello from Contact page")
