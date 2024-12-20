# Generated by Django 5.1.2 on 2024-11-11 17:03

import apps.users.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shelter',
            name='password',
            field=models.CharField(default='default_password', max_length=100, validators=[apps.users.validators.senha_safety]),
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='default_password', max_length=100, validators=[apps.users.validators.senha_safety]),
        ),
    ]
