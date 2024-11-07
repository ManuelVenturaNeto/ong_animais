from django.core.exceptions import ValidationError
from datetime import datetime
from validate_docbr import CPF, CNPJ

def birthday_valid(value):
    if value >= datetime.now().date():
        raise ValidationError("A data de nascimento está no futuro.")

def cpf_validator(numero_cpf):
    cpf = CPF()
    