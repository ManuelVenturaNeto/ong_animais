from django import forms
from .models import Address, User, Shelter
from .consulta_ibge import unidade_federativa, municipios_por_uf
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Usuário", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Senha", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    login_type = forms.ChoiceField(choices=[('user', 'Usuário'), ('shelter', 'Abrigo')], widget=forms.Select(attrs={'class': 'form-control'}))


class AddressForm(forms.ModelForm):
    state = forms.ChoiceField(choices=unidade_federativa())
    city = forms.ChoiceField(choices=[])

    class Meta:
        model = Address
        fields = '__all__'
        labels = {
            'country': 'País',
            'zip_code': 'CEP',
            'state': 'Estado',
            'city': 'Cidade',
            'neighborhood': 'Bairro',
            'street': 'Rua',
            'number': 'Numero',
            'complement': 'Complemento',
        }
        widgets = {
            'country': forms.Select(attrs={'class': 'form-control'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
            'city': forms.Select(attrs={'class': 'form-control'}),
            'neighborhood': forms.TextInput(attrs={'class': 'form-control'}),
            'street': forms.TextInput(attrs={'class': 'form-control'}),
            'number': forms.TextInput(attrs={'class': 'form-control'}),
            'complement': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        state = self.initial.get('state')
        if state:
            self.fields['city'].choices = municipios_por_uf(state)


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ['creat_at']
        labels = {
            'name': 'Nome',
            'cpf': 'CPF',
            'phone': 'Numero de Celular',
            'email': 'Email',
            'birthday': 'Data de Nascimento',
            'terms': 'Concorda com os termos de adesão',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'cpf': forms.TextInput(attrs={'class':'form-control'}),
            'phone': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'birthday': forms.DateInput(attrs={'class':'form-control'}),
            'terms': forms.CheckboxInput(attrs={'class':'form-control'}),
        }
        
        
class ShelterForm(forms.ModelForm):
    class Meta:
        model = Shelter
        exclude = ['creat_at']
        labels = {
            'name': 'Nome',
            'cpf': 'CPF',
            'phone': 'Numero de Celular',
            'email': 'Email',
            'birthday': 'Data de Nascimento',
            'terms': 'Concorda com os termos de adesão',
        }
        widgets = {
            'responsible_name': forms.TextInput(attrs={'class':'form-control'}),
            'responsible_cpf': forms.TextInput(attrs={'class':'form-control'}),
            'responsible_phone': forms.TextInput(attrs={'class':'form-control'}),
            'responsible_email': forms.TextInput(attrs={'class':'form-control'}),
            'responsible_birthday': forms.DateInput(attrs={'class':'form-control'}),
            
            'shelter_name': forms.TextInput(attrs={'class':'form-control'}),
            'shelter_cnpj': forms.TextInput(attrs={'class':'form-control'}),
            'shelter_phone': forms.TextInput(attrs={'class':'form-control'}),
            'shelter_email': forms.TextInput(attrs={'class':'form-control'}),
            
            'terms': forms.CheckboxInput(attrs={'class':'form-control'}),
        }
