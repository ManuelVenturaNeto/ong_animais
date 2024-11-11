from django.core.exceptions import ValidationError
from datetime import datetime
from validate_docbr import CPF, CNPJ
from django.contrib.auth.password_validation import validate_password

def birthday_valid(value):
    if value >= datetime.now().date():
        raise ValidationError("A data de nascimento está no futuro.")

def cpf_validator(numero_cpf):
    cpf = CPF()
    if not cpf.validate(numero_cpf):
        raise ValidationError("CPF inválido.")

def cnpj_validator(numero_cnpj):
    cnpj = CNPJ()
    if numero_cnpj is not None:
        if not cnpj.validate(numero_cnpj):
            raise ValidationError("CNPJ inválido.")

def senha_safety(senha):
    try:
        validate_password(senha)
        print("Senha válida!")
    except ValidationError as e:
        print("Erros de validação:", e.messages)

        