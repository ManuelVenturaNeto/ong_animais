from django.shortcuts import render, get_object_or_404, redirect
from .models import Pet
from .forms import PetForms
from django.contrib import messages
from PIL import Image
import os
# from .validators import is_image

def home(request):
    pets = Pet.objects.all()
    return render(request, 'home/home.html', {'pets': pets})

def sobre(request):
    return render(request, 'informacoes/sobre.html')

def contato(request):
    return render(request, 'informacoes/contato.html') 

def register_pet(request):
    if not request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = PetForms(request.POST, request.FILES)
        if form.is_valid():
            pet = form.save(commit=False)  # Salva a instância sem escrever no banco
            pet.save()  # Salva no banco para obter o caminho da imagem

            if pet.foto:
                img = Image.open(pet.foto.path)
                width, height = img.size
                
                # if is_image(img.format) == (False,):
                #     return messages.error(f'O Formato é invalido')
                
                # Define a proporção alvo
                target_aspect_ratio = 150 / 100
                current_aspect_ratio = width / height

                if current_aspect_ratio < target_aspect_ratio:
                    # Caso a imagem seja mais alta que larga, corta em cima e embaixo
                    new_height = int(width / target_aspect_ratio)
                    top = (height - new_height) // 2
                    bottom = top + new_height
                    img = img.crop((0, top, width, bottom))  # Recorte vertical centralizado

                elif current_aspect_ratio > target_aspect_ratio:
                    # Caso a imagem seja mais larga que alta, corta nas laterais
                    new_width = int(height * target_aspect_ratio)
                    left = (width - new_width) // 2
                    right = left + new_width
                    img = img.crop((left, 0, right, height))  # Recorte horizontal centralizado

                # Redimensiona para 150x100 mantendo a qualidade
                img = img.resize((150, 100), Image.LANCZOS)
                img.save(pet.foto.path, quality=90, optimize=True, )  # Salva a imagem processada #exif=img.info.get('exif')

            return redirect('home')  # Redireciona após o cadastro bem-sucedido
    else:
        form = PetForms()

    return render(request, 'pets/register_pet.html', {'form': form})

def delete_pet(request, foto_id):
    pet = Pet.objects.get(id=foto_id)
    pet.delete()
    messages.success(request, "Pet deletado com sucesso")
    return redirect('home')

def edit_pet(request, foto_id):
    pet = Pet.objects.get(id=foto_id)
    form = PetForms(instance=pet)
    
    if request.method == 'POST':
        form = PetForms(request.POST, request.FILES, instance=pet)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pet editado com sucesso')
            return redirect('home')
    return render(request, 'pets/edit_pet.html', {'form': form, 'foto_id': foto_id})