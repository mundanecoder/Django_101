from django.http import HttpResponse

def home(request):
    return HttpResponse("hello world")

def about(request):
    return HttpResponse("Hello from About page")

def contact(request):
    return HttpResponse("Hello from Contact page")
