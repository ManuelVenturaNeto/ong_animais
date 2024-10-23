from django.db import models

class Pet(models.Model):
    CATEGORIA = [('Can','Canino'), ('Fel','Felino'), ('Ave','Ave'), ('rep','Réptil')]
    nome = models.CharField(max_length=50)
    categoria = models.CharField(max_length=3, choices=CATEGORIA)
    foto = models.ImageField(upload_to="foto/%Y/%m/%d/", blank=True)
    def __str__(self):
        return self.nome
    def get_categoria_display(self):
        # Este método retorna o texto legível da categoria
        return dict(self.CATEGORIA).get(self.categoria, "Categoria Desconhecida")

class usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    telefone = models.CharField(max_length=15)
    def __str__(self):
        return self.nome