from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django import forms
from .models import *
import datetime



class CompanyRegistrationForm(UserCreationForm):
    """
    Form for registering a company.
    """

    class Meta:
        model = User
        fields = ('username', 'email')
        labels = {
            'username': 'Company Name',
            'email': 'Company Email',
        }

    def save(self, commit=True):
        """
        Save the company and user.
        """
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
    """
    Form for logging in a user.
    """
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
    """
    Form for setting up a company."""
    class Meta:
        model = Company
        fields = ['address', 'email', 'phone', 'website', 'logo']


class DepartmentForm(forms.ModelForm):
    """
    Form for creating a department.
    """
    class Meta:
        model = Department
        fields = ['name', 'abbreviation']


class TitleForm(forms.ModelForm):
    """
    Form for creating a title.
    """
    class Meta:
        model = Title
        fields = ['name', 'abbreviation']

class ContractForm(forms.ModelForm):
    """
    Form for creating a contract type.
    """
    class Meta:
        model = Contract_type
        fields = ['name', 'abbreviation']

class PositionForm(forms.ModelForm):
    """
    Form for creating a position.
    """
    class Meta:
        model = Position
        fields = ['name', 'abbreviation']

class EmployeeForm(forms.ModelForm):
    """
    Form for creating an employee.
    """
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
    """
    Form for editing a department.
    """
    class Meta:
        model = Department
        fields = ['name', 'abbreviation']
  