from django.db import models
from datetime import datetime
from .validators import birthday_valid

class Pet(models.Model):
    CATEGORY_CHOICES = [('Can','Canino'), ('Fel','Felino'), ('Ave','Ave'), ('rep','Réptil')]
    
    name = models.CharField(max_length=50, blank=False, null=False)
    category = models.CharField(max_length=3, choices=CATEGORY_CHOICES, blank=False, null=False)
    photo = models.ImageField(upload_to="photo/%Y/%m/%d/", blank=False, null=False)
    description = models.TextField(max_length=1500, blank=True)
    birthday = models.DateField(default=datetime.now, validators=[birthday_valid])
    creat_at = models.DateTimeField(default=datetime.now)
    
    def __str__(self):
        return self.name
    
    def get_category_display(self):
        return dict(self.CATEGORY_CHOICES).get(self.category, "Categoria Desconhecida")
