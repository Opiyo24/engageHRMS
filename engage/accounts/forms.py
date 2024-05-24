from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *

class AccountCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(AccountCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs.update({'class': 'form-control'})


class CompanyAccountForm(forms.ModelForm):
    class Meta:
        model = Company_account
        fields = ['company_name', 'password1', 'password2']


class CompanySetUpForm(forms.ModelForm):
    class Meta:
        model = Company_account
        exclude = ['company_name', 'password1', 'password2']
        # fields = '__all__'

class CompanyLoginForm(forms.ModelForm):
    class Meta:
        model = Company_account
        fields = ['company_name', 'password1']

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['department_name', 'department_abbreviation']


class TitleForm(forms.ModelForm):
    class Meta:
        model = Title
        fields = ['title_name', 'title_abbreviation']

class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract_type
        fields = ['contract_type', 'contract_abbreviation']

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['title', 'first_name', 'last_name', 'email', 'phone', 'department', 'position', 'title', 'contract_type', 'start_date', 'end_date', 'salary']
  