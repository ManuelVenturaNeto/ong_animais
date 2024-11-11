from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages, auth
from .forms import AddressForm, UserForm, ShelterForm # LoginForm

def login(request):
    return render(request, 'user/login.html')

def register_user(request):
    form_user = UserForm()
    form_address = AddressForm()
    if request.method == 'POST':
        form_user = UserForm(request.POST)
        form_address = AddressForm(request.POST)
        if form_user.is_valid() and form_address.is_valid:
            # form_user.save()
            # form_address.save()
            pass
    return render(request, 'user/register_user.html', {'form_user': form_user, 'form_address': form_address})

def register_shelter(request):
    return render(request, 'user/register_shelter.html')

def logout(request):
    return render(request, '')

# def apply_login(request):
#     form = LoginForm()
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             pass
#     return render(request, '/login.html', {'form': form})

