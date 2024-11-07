from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages, auth
from PIL import Image

def login(request):
    return render(request, 'user/login.html')

def register_user(request):
    return render(request, 'user/register_user.html')

def register_shelter(request):
    return render(request, 'user/register_shelter.html')

def logout(request):
    return render(request, '')