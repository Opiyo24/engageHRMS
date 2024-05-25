from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = '__all__' 

# class AccountCreationForm(UserCreationForm):
#     def __init__(self, *args, **kwargs):
#         super(AccountCreationForm, self).__init__(*args, **kwargs)

#         for fieldname in ['username', 'password1', 'password2']:
#             self.fields[fieldname].help_text = None
#             self.fields[fieldname].widget.attrs.update({'class': 'form-control'})


class CompanyRegistrationForm(UserCreationForm):
    # name = forms.CharField(max_length=255)
    # password = forms.CharField(max_length=255)

    class Meta:
        model = User
        fields = ('username', 'email')
        labels = {
            'username': 'Company Name',
            'email': 'Company Email',
        }

    def save(self, commit=True):
        user = super(CompanyRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.is_staff = True
        if commit:
            user.save()
            company = Company.objects.create(name=self.cleaned_data['name'], password=self.cleaned_data['password'], owner=user)
            company.save()
            user.company = company
            user.save()

        return user


class CompanySetUpForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['address', 'email', 'phone', 'website', 'logo']

# class CompanyLoginForm(forms.ModelForm):
#     class Meta:
#         model = Company
#         fields = ['name', 'password']

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'abbreviation']


class TitleForm(forms.ModelForm):
    class Meta:
        model = Title
        fields = ['name', 'abbreviation']

class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract_type
        fields = ['contract_type', 'abbreviation']

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['title', 'first_name', 'last_name', 'email', 'phone', 'department', 'position', 'title', 'contract_type', 'start_date', 'end_date', 'salary']
  