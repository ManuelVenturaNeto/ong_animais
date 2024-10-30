from django.shortcuts import render, get_object_or_404, redirect
from .models import Pet
from .forms import PetForms
from django.contrib import messages
from PIL import Image
import os

def home(request):
    pets = Pet.objects.all()
    return render(request, 'home/home.html', {'pets': pets})

def sobre(request):
    return render(request, 'informacoes/sobre.html')

def contato(request):
    return render(request, 'informacoes/contato.html')

"""
def cadastra_pet(request):
    if not request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = PetForms(request.POST, request.FILES)
        if form.is_valid():
            pet = form.save(commit=False)  # Salva a instância sem escrever no banco
            pet.save()  # Salva a instância no banco para obter o caminho da imagem
            
            if pet.foto:  # Verifica se a imagem foi enviada
                img = Image.open(pet.foto.path)  # Abre a imagem
                size = (150, 100)
                img = img.resize(size, Image.LANCZOS)  # Substitui Image.ANTIALIAS por Image.LANCZOS
                img.save(pet.foto.path)  # Salva a imagem recortada

            return redirect('pet_list')  # Redireciona após o cadastro bem-sucedido
    else:
        form = PetForms()  # Inicializa um novo formulário

    return render(request, 'pets/cadastra_pet.html', {'form': form})
"""

def registra_pet(request):
    if not request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = PetForms(request.POST, request.FILES)
        if form.is_valid():
            pet = form.save(commit=False)  # Salva a instância sem escrever no banco
            pet.save()  # Salva a instância no banco para obter o caminho da imagem
            
            if pet.foto:  # Verifica se a imagem foi enviada
                img = Image.open(pet.foto.path)  # Abre a imagem
                width, height = img.size
                
                tamanho_ideal = 150/100
                tamanho_aceitavel_maior = tamanho_ideal*1.2
                tamanho_aceitavel_menor = tamanho_ideal*0.8
                
                if not (width/ height) == 150/100:
                    if ((width/ height) < tamanho_aceitavel_menor) or ((width/ height) > tamanho_aceitavel_maior):
                        #essa logica ainda não funciona. corrigir
                        if height > width:
                            # Define a área de recorte 150x100 centralizada
                            left = width / 2
                            top = (width * 1.5) / 2
                            right = width / 2
                            bottom = (width * 1.5) / 2
                            img = img.crop((left, top, right, bottom))  # Realiza o recorte
                        else:
                            left = (height * (2/3)) / 2
                            top = height / 2
                            right = (height * (2/3)) / 2
                            bottom = height / 2
                            img = img.crop((left, top, right, bottom))  # Realiza o recorte
                    else:
                        size = (150, 100)
                        img = img.resize(size, Image.LANCZOS)  # Substitui Image.ANTIALIAS por Image.LANCZOS
                        
                img.save(pet.foto.path)  # Salva a imagem recortada

            return redirect('home')  # Redireciona após o cadastro bem-sucedido
    else:
        form = PetForms()  # Inicializa um novo formulário

    return render(request, 'pets/cadastra_pet.html', {'form': form})

def deleta_pet(request, foto_id):
    pet = Pet.objects.get(id=foto_id)
    pet.delete()
    messages.success(request, "Pet deletado com sucesso")
    return redirect('home')