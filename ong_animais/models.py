from django.db import models

class Pet(models.Model):
    CATEGORIA = [('Can','Canino'), ('Fel','Felino'), ('Ave','Ave'), ('rep','Réptil')]
    nome = models.CharField(max_length=50)
    categoria = models.CharField(max_length=3, choices=CATEGORIA)

class usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    telefone = models.CharField(max_length=15)