from django.shortcuts import render, HttpResponse

# Create your views here.
def index(requst):
    return HttpResponse("Welcome, to ENGAGE HRMS")

def register(request):
    return render(request, 'registration/base.html')
