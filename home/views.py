from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')

def contact(request):
    return HttpResponse("CONTACTPAGE")

def about(request):
    return HttpResponse("ABOUTPAGE")