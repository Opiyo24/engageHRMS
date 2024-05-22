from django.shortcuts import render, redirect
#import usercreation form
from .forms import AccountCreationForm, CompanyAccountForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError

# Create your views here.
def signup(request):
    if request.method == "GET":
        return render(request, 'accounts/signup.html', {'form': AccountCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('registration-index')
            except IntegrityError:
                return render(request, 'accounts/signup.html', {'form': AccountCreationForm, 'error': 'That username has already been taken.'})
        else:
            return render(request, 'accounts/signup.html', {'form': AccountCreationForm, 'error': 'Passwords must match'})
        

def company_creation(request):
    if request.method == 'POST':
        company_form = CompanyAccountForm(request.POST, request.FILES)
        if company_form.is_valid():
            company_form.save()
            return redirect('some_view_name')  # Redirect to a success page or some other view
    else:
        company_form = CompanyAccountForm()
    
    return render(request, 'accounts/company_signup.html', {'company_form': company_form})
    # context = {}
    # company_form = CompanyAccountForm()
    # context = {
    #     'c_form' : company_form
    # }
    # if request.method == "GET":
    #     return render(request, 'accounts/signup.html', {'c_form': company_form})
    # else:
    #     if request.POST['password1'] == request.POST['password2']:
    #         try:
    #             user = User.objects.create_user(request.POST['companyname'], password=request.POST['password1'])
    #             user.save()
    #             login(request, user)
    #             return redirect('registration-index')
    #         except IntegrityError:
    #             return render(request, 'accounts/compoany_signup.html', {'c_form': company_form, 'error': 'That username has already been taken.'})
    #     else:
    #         return render(request, 'accounts/company_signup.html', {'c_form': company_form, 'error': 'Passwords must match'})


