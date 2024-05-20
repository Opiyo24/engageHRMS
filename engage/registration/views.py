from django.shortcuts import render, HttpResponse, redirect
from .forms import UserForm, LoginForm, CompanyForm, CompanyLoginForm


# Create your views here.
def index(request):
    return render(request, 'registration/base.html')

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('registration-index')
    else:
        form = UserForm()
    context = {'form': form, 'title': 'Registration Form'}
    return render(request, 'registration/register.html', context)


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('registration-index')
    else:
        form = LoginForm()
    context = {'form': form, 'title': 'Login Form'}
    return render(request, 'registration/login.html', context)

def user_logout(request):
    pass


def comapny_login(request):
    pass

def comapny_logout(request):
    pass
