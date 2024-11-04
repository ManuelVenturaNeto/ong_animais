from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from PIL import Image

def users(request):
    return render(request, 'users.html')