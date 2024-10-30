from django.shortcuts import render, get_object_or_404, redirect
from .models import Pet
from .forms import PetForms
from django.contrib import messages

def home(request):
    pets = Pet.objects.all()
    return render(request, 'home/home.html', {'pets': pets})

def sobre(request):
    return render(request, 'informacoes/sobre.html')

def contato(request):
    return render(request, 'informacoes/contato.html')

def cadastra_pet(request):
    if not request.user.is_authenticated:
        return redirect('home')
    form = PetForms
    
    if request.method == 'POST':
        form = PetForms(request.POST, request.FILES)
        if form.is_valid:
            form.save()
    return render(request, 'pets/cadastra_pet.html', {'form': form})

def deleta_pet(request):
    return render(request, 'pets/deleta_pet.html')