from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django import forms
from .models import *
import datetime

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
            company = Company.objects.create(name=self.cleaned_data['username'], password=self.cleaned_data['password1'], owner=user)
            company.save()
            user.company = company
            user.save()

        return user
    
class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255, widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError('Invalid username or password')
        return self.cleaned_data


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
        fields = ['name', 'abbreviation']

class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = ['name', 'abbreviation']

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            'number', 'title', 'first_name', 'last_name', 'email', 'phone', 'address', 'position', 'department', 'contract_type', 'salary', 'status', 'shift', 'start_date', 'end_date', 'profile_picture',
        ]
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date', 'max': datetime.date.today().isoformat()}),
            'end_date': forms.DateInput(attrs={'type': 'date', max: datetime.date.today().isoformat()}),
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        
        if 'company' in self.data:
            try:
                company_id = int(self.data.get('company'))
                self.fields['department'].queryset = Department.objects.filter(company_id=company_id).order_by('name')
                self.fields['title'].queryset = Title.objects.filter(company_id=company_id).order_by('name')
                self.fields['position'].queryset = Position.objects.filter(company_id=company_id).order_by('name')
                self.fields['contract_type'].queryset = Contract_type.objects.filter(company_id=company_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty queryset
        elif self.instance.pk:
            self.fields['department'].queryset = self.instance.company.department_set.order_by('name')
            self.fields['title'].queryset = self.instance.company.title_set.order_by('name')
            self.fields['position'].queryset = self.instance.company.position_set.order_by('name')
            self.fields['contract_type'].queryset = self.instance.company.contract_type_set.order_by('name')

class EditDeptForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'abbreviation']
  