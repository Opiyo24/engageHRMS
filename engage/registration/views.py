from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'registration/index.html')

def register(request):
    return render(request, 'registration/register.html')
