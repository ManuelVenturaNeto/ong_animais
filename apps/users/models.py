from django.db import models
from .validators import birthday_valid, cpf_validator, cnpj_validator, senha_safety
from django.utils import timezone
from .consulta_ibge import unidade_federativa
 

class Address(models.Model):
    COUNTRY = [
        ('BR', 'Brasil')
    ]
    country = models.CharField(max_length=2, choices=COUNTRY)
    zip_code = models.CharField(max_length=8)
    state = models.CharField(max_length=2, choices=unidade_federativa)
    city = models.CharField(max_length=50)
    neighborhood = models.CharField(max_length=100)
    street = models.CharField(max_length=255)
    number = models.CharField(max_length=10, blank=True, null=True)
    complement = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.street}, {self.number} - {self.neighborhood}, {self.city}/{self.state} - {self.zip_code}'

class User(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100, validators=[senha_safety])
    cpf = models.CharField(max_length=11, unique=True, validators=[cpf_validator])
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=150)
    birthday = models.DateField(validators=[birthday_valid])
    terms = models.BooleanField()
    id_address = models.OneToOneField(Address, on_delete=models.CASCADE)
    creat_at = models.DateTimeField(default=timezone.now)
    
class Shelter(models.Model):
    responsible_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100, validators=[senha_safety])
    responsible_cpf = models.CharField(max_length=11, unique=True)
    responsible_phone = models.CharField(max_length=15)
    responsible_email = models.EmailField(max_length=150)
    responsible_birthday = models.DateField(validators=[birthday_valid])
    
    shelter_name = models.CharField(max_length=100,)
    shelter_cnpj = models.CharField(max_length=14, unique=True, validators=[cnpj_validator])
    shelter_phone = models.CharField(max_length=15)
    shelter_email = models.EmailField(max_length=150)
    
    id_address = models.OneToOneField(Address, on_delete=models.CASCADE)
    terms = models.BooleanField()
    creat_at = models.DateTimeField(default=timezone.now)