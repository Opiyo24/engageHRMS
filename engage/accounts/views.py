from django.shortcuts import render, redirect, get_object_or_404
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


def company_set_up_intro(request):
    return render(request, 'accounts/set_up_intro.html')

def company_set_up(request):
    company = request.user.company
    if request.method == 'POST':
        set_up_form = CompanySetUpForm(request.POST, instance=company)

        if set_up_form.is_valid():
            set_up_form.save()

            messages.success(request, 'Profile updated successfully')
            return render(request, 'accounts/logged_in.html')  # Redirect to a specific view after successful submission
    else:
        set_up_form = CompanySetUpForm()


    context = {
        'set_up_form': set_up_form,
    }
    return render(request, 'accounts/company.html', context)

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, 'Welcome back!')
                return redirect('accounts:company-logged')
    else:
        form = LoginForm()
    return render(request, 'accounts/company_login.html', {'form': form})


def logout_view(request):
    form = LoginForm()
    logout(request)
    return render(request, 'accounts/company_login.html', {'form': form})


######################## DEPARTMENT ############################
def add_dept(request):
    context = {}
    departments = Department.objects.filter(company=request.user.company)
    if request.method == 'POST':
        dept_form = DepartmentForm(request.POST)
        if dept_form.is_valid():
            department = dept_form.save(commit=False)
            department.company = request.user.company
            department.save()
            messages.success(request, 'Department added successfully')
        else:
            messages.error(request, 'Department not added')
    context = {
        'dept_form': DepartmentForm,
        'departments': departments,
        }
    return render(request, 'accounts/add_dept.html', context)

def add_position(request):
    context = {}
    positions = Position.objects.filter(company=request.user.company)
    if request.method == 'POST':
        position_form = PositionForm(request.POST)
        if position_form.is_valid():
            position = position_form.save(commit=False)
            position.company = request.user.company
            position.save()
            messages.success(request, 'Position added successfully')
        else:
            messages.error(request, 'Position not added')
    context = {
        'position_form': PositionForm,
        'positions': positions,
        }
    return render(request, 'accounts/add_position.html', context)

def add_contract_type(request):
    context = {}
    contracts = Contract_type.objects.filter(company=request.user.company)
    if request.method == 'POST':
        contract_form = ContractForm(request.POST)
        if contract_form.is_valid():
            contract_type = contract_form.save(commit=False)
            contract_type.company = request.user.company
            contract_type.save()
            messages.success(request, 'Contract type added successfully')
        else:
            messages.error(request, 'Contract type not added')
    else:
        contract_form = ContractForm()

    context = {
        'contract_form': contract_form,
        'contracts': contracts,
        }   
    return render(request, 'accounts/add_contract_type.html', context)

def add_title(request):
    context = {}
    titles = Title.objects.filter(company=request.user.company)
    if request.method == 'POST':
        title_form = TitleForm(request.POST)
        if title_form.is_valid():
            title = title_form.save(commit=False)
            title.company = request.user.company
            title.save()
            messages.success(request, 'Title added successfully')
        else:
            messages.error(request, 'Title not added')
    context = {
        'title_form': TitleForm,
        'titles': titles,
        }
    return render(request, 'accounts/add_title.html', context)

def add_employee(request):
    context = {}
    employees = Employee.objects.filter(company=request.user.company)
    comp = get_object_or_404(Company, pk=request.user.company.id)
    if request.method == 'POST':
        emp_form = EmployeeForm(request.POST)
        if emp_form.is_valid():
            employee = emp_form.save(commit=False)
            employee.company = request.user.company
            employee.save()
            messages.success(request, 'Employee added successfully')
        else:
            messages.error(request, 'Employee not added')
    else:
        emp_form = EmployeeForm()

    context = {
        'emp_form': emp_form,
        'employees': employees,
        'company_id': comp.id,
        }
    return render(request, 'accounts/add_employee.html', context)

def remove_dept(request):
    return render(request, 'accounts/remove_dept.html')

def remove_position(request):
    return render(request, 'accounts/remove_position.html')

def remove_contract_type(request):
    return render(request, 'accounts/remove_contract_type.html')

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
