from django.shortcuts import render, HttpResponse, redirect
from .forms import UserForm, LoginForm, CompanyForm, CompanyLoginForm, EmployeeForm, EmployeeLoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.

def index(request):
    return render(request, 'registration/index.html', {'title':'Home'})

############# USER #############

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
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print("The user is authenticated")
            else:
                print("The user is not authenticated")
            form.save()
            return redirect('registration-index')
    else:
        form = LoginForm()
    context = {'form': form, 'title': 'Login Form'}
    return render(request, 'registration/login.html', context)

@login_required
def user_logout(request):
    logout(request)
    return redirect('registration-index')

############# COMPANY #############
def company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('registration-index')
    else:
        form = CompanyForm()
    context = {'form': form, 'title': 'Company Registration Form'}
    return render(request, 'registration/company.html', context)

def company_login(request):
    if request.method == 'POST':
        form = CompanyLoginForm(request.POST)

        if form.is_valid():
            companyname = form.cleaned_data['companyname']
            password = form.cleaned_data['password']
            user = authenticate(request, username=companyname, password=password)
            if user is not None: #and user.is_staff:
                login(request, companyname)
                return redirect('registration-index')
            else:
                messages.error(request, 'Invalid company name or password')
    else:
        form = CompanyLoginForm()
    context = {'form': form, 'title': 'Company Login Form'}
    return render(request, 'registration/company_login.html', context)

@login_required
def comapny_logout(request):
    logout(request)
    return redirect('registration-index')

############# EMPLOYEE #############

def employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('registration-index')
    else:
        form = EmployeeForm()
    context = {'form': form, 'title': 'Employee Registration Form'}
    return render(request, 'registration/employee.html', context)

def employee_login(request):
    if request.method == 'POST':
        form = EmployeeLoginForm(request.POST)

        if form.is_valid():
            employeeusername = form.cleaned_data['employeeusername']
            employeepassword = form.cleaned_data['employeepassword']
            user = authenticate(request, username=employeeusername, password=employeepassword)
            if user is not None:
                login(request, employeeusername)
                return redirect('registration-index')
            else:
                messages.error(request, 'Invalid employee name or password')
    else:
        form = EmployeeLoginForm()
    context = {'form': form, 'title': 'Employee Login Form'}
    return render(request, 'registration/employee_login.html', context)

@login_required
def employee_logout(request):
    logout(request)
    return redirect('registration-index')


def user_profile(request):
    context = {
        'title': 'User Profile',
        }
    return render(request, 'registration/user_profile.html', context)

def employee_profile(request):
    context = {
        'title': 'Employee Profile',
        }
    return render(request, 'registration/employee_profile.html', context)

def company_profile(request):
    context = {
        'title': 'Company Profile',
        }
    return render(request, 'registration/company_profile.html', context)
