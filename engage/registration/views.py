from django.shortcuts import render, HttpResponse

# Create your views here.
def register(request):
    return HttpResponse("Hello, world. You're at the registration index.")
