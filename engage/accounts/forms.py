from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Company_account

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
  