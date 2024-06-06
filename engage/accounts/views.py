from django.shortcuts import render, redirect, get_object_or_404
#import usercreation form
from django.http import JsonResponse, HttpResponse, HttpRequest
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.contrib import messages
from django.template.loader import render_to_string
from django.views.generic import UpdateView
from django.urls import reverse_lazy
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

def delete_dept(request, pk):
    department = Department.objects.get(pk=pk)
    department.delete()
    return redirect('accounts:add_dept')

class DepartmentUpdateView(UpdateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'accounts/edit_dept.html'
    success_url = reverse_lazy('accounts:add_dept')

    def form_valid(self, form):
        department = form.save(commit=False)
        department.company = self.request.user.company
        department.save()
        messages.success(self.request, 'Department updated successfully')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['department'] = self.object
        return context

def delete_position(request, pk):
    position = Position.objects.get(pk=pk)
    position.delete()
    return redirect('accounts:add_position')


def delete_contract_type(request, pk):
    contract_type = Contract_type.objects.get(pk=pk)
    contract_type.delete()
    return redirect('accounts:add_contract_type')

def delete_title(request, pk):
    title = Title.objects.get(pk=pk)
    title.delete()
    return redirect('accounts:add_title')


def delete_employee(request, pk):
    employee = Employee.objects.get(pk=pk)
    employee.delete()
    return redirect('accounts:add_employee')


def logged(request):
    return render(request, 'accounts/logged_in.html')


def dashboard(request):
    deptn = Department.objects.filter(company=request.user.company).count()
    empn = Employee.objects.filter(company=request.user.company).count()
    name = request.user.company.name
    logo = request.user.company.logo
    employees = Employee.objects.filter(company=request.user.company)

    context = {
        'deptn': deptn,
        'empn': empn,
        'name': name,
        'logo': logo,
        'employees': employees,
    }
    return render(request, 'accounts/accounts_dashboard.html', context)

def calendar(request):
    return render(request, 'accounts/calendar.html')

class TitleUpdateView(UpdateView):
    model = Title
    form_class = TitleForm
    template_name = 'accounts/edit_title.html'
    success_url = reverse_lazy('accounts:add_title')

    def form_valid(self, form):
        title = form.save(commit=False)
        title.company = self.request.user.company
        title.save()
        messages.success(self.request, 'Title updated successfully')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object
        return context


class ContractTypeUpdateView(UpdateView):
    model = Contract_type
    form_class = ContractForm
    template_name = 'accounts/edit_contract_type.html'
    success_url = reverse_lazy('accounts:add_contract_type')

    def form_valid(self, form):
        contract_type = form.save(commit=False)
        contract_type.company = self.request.user.company
        contract_type.save()
        messages.success(self.request, 'Contract type updated successfully')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contract_type'] = self.object
        return context


class PositionUpdateView(UpdateView):
    model = Position
    form_class = PositionForm
    template_name = 'accounts/edit_position.html'
    success_url = reverse_lazy('accounts:add_position')

    def form_valid(self, form):
        position = form.save(commit=False)
        position.company = self.request.user.company
        position.save()
        messages.success(self.request, 'Position updated successfully')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['position'] = self.object
        return context


class EmployeeUpdateView(UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'accounts/edit_employee.html'
    success_url = reverse_lazy('accounts:add_employee')

    def form_valid(self, form):
        employee = form.save(commit=False)
        employee.company = self.request.user.company
        employee.save()
        messages.success(self.request, 'Employee updated successfully')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employee'] = self.object
        return context
