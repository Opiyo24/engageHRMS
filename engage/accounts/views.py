from django.shortcuts import render, redirect
#import usercreation form
from django.http import HttpResponse, HttpRequest
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.contrib import messages
from .models import *

# Create your views here.
def home(request):
    context = {}
    return render(request, 'accounts/home.html', context)

# def signup(request):
#     if request.method == "GET":
#         return render(request, 'accounts/signup.html', {'form': AccountCreationForm})
#     else:
#         if request.POST['password1'] == request.POST['password2']:
#             try:
#                 user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
#                 user.save()
#                 login(request, user)
#                 return redirect('registration-index')
#             except IntegrityError:
#                 return render(request, 'accounts/signup.html', {'form': AccountCreationForm, 'error': 'That username has already been taken.'})
#         else:
#             return render(request, 'accounts/signup.html', {'form': AccountCreationForm, 'error': 'Passwords must match'})
        
##################### COMPANY #########################
def company_creation(request):

    if request.method == 'POST':
        print("At begining")
        company_form = CompanyRegistrationForm(request.POST)
        if company_form.is_valid():
            print("In loop")
            # company_form.save()
            print("Copmany created")
            user = company_form.save()
            login(request, user)
            messages.success(request, 'Company created!')
            return render(request, 'accounts/set_up_intro.html')
        else:
            print(company_form.errors)
    else:
        company_form = CompanyRegistrationForm()
        print("Company not created")
    
    return render(request, 'accounts/company_signup.html', {'company_form': company_form})

# def company_login(request):
#     if request.method == 'POST':
#         authentication_form = CompanyLoginForm(request.POST)
#         if authentication_form.is_valid():
#             company_name = authentication_form.cleaned_data['company_name']
#             password = authentication_form.cleaned_data['password1']
#             user = authenticate(request, company_name=company_name, password=password)
#             if Company is not None:
#                 login(request, user)
#                 return render(request, 'accounts/logged_in.html')
#             else:
#                 return render(request, 'accounts/company_login.html', {'authentication_form': authentication_form, 'error': 'Invalid credentials'})
#     return render(request, 'accounts/company_login.html', {'form': CompanyLoginForm})

def company_set_up_intro(request):
    return render(request, 'accounts/set_up_intro.html')

def company_set_up(request):
    company = request.user.company
    if request.method == 'POST':
        set_up_form = CompanySetUpForm(request.POST, instance=company)
        dept_form = DepartmentForm(request.POST)
        title_form = TitleForm(request.POST)
        contract_form = ContractForm(request.POST)
        
        if set_up_form.is_valid() and dept_form.is_valid() and title_form.is_valid() and contract_form.is_valid():
            set_up_form.save()
            dept_form.save()
            title_form.save()
            contract_form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect(request, 'accounts/logged')  # Redirect to a specific view after successful submission
    else:
        set_up_form = CompanySetUpForm()
        dept_form = DepartmentForm()
        title_form = TitleForm()
        contract_form = ContractForm()

    context = {
        'set_up_form': set_up_form,
        'dept_form': dept_form,
        'title_form': title_form,
        'contract_form': contract_form,
    }
    return render(request, 'accounts/company.html', context)


######################## DEPARTMENT ############################
def add_dept(request):
    context = {}
    if request.method == 'POST':
        dept_form = DepartmentForm(request.POST)
        if dept_form.is_valid():
            dept_form.save()
            # department.company = request.user.company
            # department.save()
            messages.success(request, 'Department added successfully')
        else:
            messages.error(request, 'Department not added')
    context = {'dept_form': DepartmentForm}
    return render(request, 'accounts/add_dept.html', context)

def add_position(request):
    return render(request, 'accounts/add_position.html')

def add_contract_type(request):
    context = {}
    if request.method == 'POST':
        contract_form = ContractForm(request.POST)
        if contract_form.is_valid():
            contract_form.save()
            # contract_type = request.user.company
            # contract_type.save()
            messages.success(request, 'Contract type added successfully')
        else:
            messages.error(request, 'Contract type not added')
    else:
        contract_form = ContractForm()

    context = {'contract_form': contract_form}   
    return render(request, 'accounts/add_contract_type.html', context)

def add_title(request):
    context = {}
    if request.method == 'POST':
        title_form = TitleForm(request.POST)
        if title_form.is_valid():
            title_form.save()
            # title.company = request.user.company
            # title.save()
            messages.success(request, 'Title added successfully')
        else:
            messages.error(request, 'Title not added')
    context = {'title_form': TitleForm}
    return render(request, 'accounts/add_title.html', context)

def remove_dept(request):
    return render(request, 'accounts/remove_dept.html')

def remove_position(request):
    return render(request, 'accounts/remove_position.html')

def remove_contract_type(request):
    return render(request, 'accounts/remove_contract_type.html')

def add_employee(request):
    context = {}
    if request.method == 'POST':
        emp_form = EmployeeForm(request.POST)
        if emp_form.is_valid():
            emp_form.save()
            messages.success(request, 'Employee added successfully')
        else:
            messages.error(request, 'Employee not added')
    context = {'emp_form': EmployeeForm}
    return render(request, 'accounts/add_employee.html', context)

def employees(request):
    return render(request, 'accounts/employees.html')

def remove_employee(request):
    return render(request, 'accounts/remove_employee.html')


def logged(request):
    return render(request, 'accounts/logged_in.html')


def dashboard(request):
    return render(request, 'accounts/profile_base.html')

def calendar(request):
    return render(request, 'accounts/calendar.html')

def add_activity(request):
    return render(request, 'accounts/add_activity.html')

def activities(request):
    return render(request, 'accounts/activities.html')

def remove_activity(request):
    return render(request, 'accounts/remove_activity.html')
