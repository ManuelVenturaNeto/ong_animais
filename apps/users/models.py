from django.db import models
from .validators import birthday_valid
import datetime
from .consulta_ibge import unidade_federativa, municipios_por_uf


class Address(models.Model):
    COUNTRY = [
        ('BR', 'Brasil')
    ]
    country = models.CharField(choices=COUNTRY)
    zip_code = models.CharField(max_length=8)
    state = models.CharField(max_length=2, choices=unidade_federativa)
    city = models.CharField(max_length=100, choices=municipios_por_uf(state))
    neighborhood = models.CharField(max_length=100)
    street = models.CharField(max_length=255)
    number = models.CharField(max_length=10, blank=True, null=True)
    complement = models.CharField(max_length=255, blank=True, null=True)
    
    

    def __str__(self):
        return f'{self.street}, {self.number} - {self.neighborhood}, {self.city}/{self.state} - {self.zip_code}'

class User(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    cpf = models.CharField(max_length=11, blank=False, null=False)
    phone = models.CharField(max_length=15, blank=False, null=False)
    email = models.EmailField(max_length=150, blank=False, null=False)
    birthday = models.DateField(default=datetime.now, validators=[birthday_valid], blank=False, null=False)
    creat_at = models.DateTimeField(default=datetime.now, blank=False, null=False)
    terms = models.BooleanField(default=False, blank=False, null=False)
    id_address = models.OneToOneField(Address, on_delete=models.CASCADE)
    
class Shelter(models.Model):
    responsible_name = models.CharField(max_length=100, blank=False, null=False)
    responsible_cpf = models.CharField(max_length=11, blank=False, null=False)
    responsible_phone = models.CharField(max_length=15, blank=False, null=False)
    responsible_email = models.EmailField(max_length=150, blank=False, null=False)
    
    shelter_name = models.CharField(max_length=100, default='Não Informado')
    shelter_cnpj = models.CharField(max_length=14, default='Não Informado')
    shelter_phone = models.CharField(max_length=15, default='Não Informado')
    shelter_email = models.EmailField(max_length=150, default='Não Informado')
    
    id_address = models.OneToOneField(Address, on_delete=models.CASCADE)
    creat_at = models.DateTimeField(default=datetime.now, blank=False, null=False)