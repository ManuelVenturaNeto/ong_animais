from django.shortcuts import render
from .models import Pet
def home(request):
    pets = Pet.objects.all()
    return render(request, 'home/home.html', {'pets': pets})

def sobre(request):
    return render(request, 'informacoes/sobre.html')

def contato(request):
    return render(request, 'informacoes/contato.html')
