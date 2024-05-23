from django.shortcuts import render, redirect
#import usercreation form
from django.http import HttpResponse, HttpRequest
from .forms import AccountCreationForm, CompanyAccountForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError

# Create your views here.
def home(request):
    context = {}
    return render(request, 'accounts/home.html', context)

def signup(request):
    if request.method == "GET":
        return render(request, 'accounts/signup.html', {'form': AccountCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('registration-index')
            except IntegrityError:
                return render(request, 'accounts/signup.html', {'form': AccountCreationForm, 'error': 'That username has already been taken.'})
        else:
            return render(request, 'accounts/signup.html', {'form': AccountCreationForm, 'error': 'Passwords must match'})
        

def company_creation(request):
    if request.method == 'POST':
        company_form = CompanyAccountForm(request.POST, request.FILES)
        if company_form.is_valid():
            company_form.save()
            return render(request, 'accounts/logged_in.html')  # Redirect to a success page or some other view
    else:
        company_form = CompanyAccountForm()
    
    return render(request, 'accounts/company_signup.html', {'company_form': company_form})

def company_set_up(request):
    return render(request, 'accounts/company.html')


def logged(request):
    return render(request, 'accounts/logged_in.html')


def profile(request):
    return render(request, 'accounts/profile_base.html')


