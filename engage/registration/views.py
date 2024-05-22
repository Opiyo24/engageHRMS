from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import CreateUserForm


# Create your views here.

def index(request):
    reg_form = CreateUserForm()

    if request.method == 'POST':
        reg_form = CreateUserForm(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            messages.success(request, 'Account created successfully')
    title = 'Registration'
    context = {'form': reg_form,
               'title':title
               }
    return render(request, 'registration/register.html', context)
