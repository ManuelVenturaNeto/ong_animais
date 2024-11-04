from django import forms
from .models import Pet

class PetForms(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'category', 'photo']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'category': forms.Select(attrs={'class':'form-control'}),
            'photo': forms.FileInput(attrs={'class':'form-control'}),
            }