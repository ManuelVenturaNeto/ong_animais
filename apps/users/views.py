from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages, auth
from .forms import LoginForm, AddressForm, UserForm,ShelterForm

def login(request):
    return render(request, 'user/login.html')

def register_user(request):
    return render(request, 'user/register_user.html')

def register_shelter(request):
    return render(request, 'user/register_shelter.html')

def logout(request):
    return render(request, '')

def apply_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():

            pass
    return render(request, 'user/login.html', {'form': form})
