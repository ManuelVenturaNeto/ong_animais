from django import forms
from .models import Pet

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['nome', 'categoria', 'foto']
    widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'categoria': forms.Select(attrs={'class':'form-control'}),
            'foto': forms.FileInput(attrs={'class':'form-control'}),
        }