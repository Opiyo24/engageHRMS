from django.shortcuts import render, HttpResponse, redirect
from .forms import UserForm


# Create your views here.
def index(request):
    return render(request, 'registration/index.html')

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
        else:
            form = UserForm()
    else:
        form = UserForm()
    return render(request, 'registration/register.html', {'form': form})


def login(request):
    return render(request, 'registration/login.html')

def logout(request):
    pass
