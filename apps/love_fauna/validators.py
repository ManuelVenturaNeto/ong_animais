from django.core.exceptions import ValidationError
from datetime import datetime

def birthday_valid(value):
    if value >= datetime.now().date():
        raise ValidationError("A data de nascimento está no futuro.")
