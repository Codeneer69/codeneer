from django.shortcuts import render, HttpResponse

# Create your views here.

def blogHome(request):
    return HttpResponse("Blog will be displayed here soon")

def blogPost(request, slug):
    return HttpResponse(f" blog post {slug}")