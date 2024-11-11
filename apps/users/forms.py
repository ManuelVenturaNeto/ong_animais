from django import forms
from .models import Address, User, Shelter
from .consulta_ibge import unidade_federativa, municipios_por_uf
from django.contrib.auth.forms import AuthenticationForm

# class LoginForm(AuthenticationForm):
#     username = forms.CharField(label="Usuário", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     password = forms.CharField(label="Senha", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
#     login_type = forms.ChoiceField(choices=[('user', 'Usuário'), ('shelter', 'Abrigo')], widget=forms.Select(attrs={'class': 'form-control'}))


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
        placeholder = {
            'country': 'Brasil',
            'zip_code': '12345-678',
            'state': 'MG',
            'city': 'Belo Horizonte',
            'neighborhood': 'Belvedere',
            'street': 'Rua do Jaraguas',
            'number': '100',
            'complement': 'Bloco C',
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ['creat_at']
        labels = {
            'name': 'Nome',
            'password': 'Senha',
            'cpf': 'CPF',
            'phone': 'Numero de Celular',
            'email': 'Email',
            'birthday': 'Data de Nascimento',
            'terms': 'Concorda com os termos de adesão',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Seu nome'}),
            'password': forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'Senha123!'}),
            'cpf': forms.TextInput(attrs={'class':'form-control', 'placeholder': '123.456.789-12'}),
            'phone': forms.TextInput(attrs={'class':'form-control', 'placeholder': '00 912345678'}),
            'email': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'email@email.com'}),
            'birthday': forms.DateInput(attrs={'class':'form-control', 'placeholder': '01/01/2000'}),
            'terms': forms.CheckboxInput(attrs={'class':'form-control'}),
        }
        
class ShelterForm(forms.ModelForm):
    class Meta:
        model = Shelter
        exclude = ['creat_at']
        labels = {
            'name': 'Nome',
            'password': 'Senha',
            'cpf': 'CPF',
            'phone': 'Numero de Celular',
            'email': 'Email',
            'birthday': 'Data de Nascimento',
            'terms': 'Concorda com os termos de adesão',
        }
        widgets = {
            'responsible_name': forms.TextInput(attrs={'class':'form-control'}),
            'passaword': forms.PasswordInput(attrs={'class':'form-control'}),
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
