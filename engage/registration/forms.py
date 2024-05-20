from django import forms
from .models import User, Company, Employee

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'


class CompanyLoginForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['companyname']

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

class EmployeeLoginForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['employeeusername', 'employeepassword']