from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from PIL import Image

def clinicas(request):
    return render(request, 'clinicas.html')
