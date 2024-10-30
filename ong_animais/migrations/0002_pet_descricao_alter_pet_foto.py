# Generated by Django 5.1.2 on 2024-10-30 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ong_animais', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='descricao',
            field=models.TextField(blank=True, max_length=1500),
        ),
        migrations.AlterField(
            model_name='pet',
            name='foto',
            field=models.ImageField(upload_to='foto/%Y/%m/%d/'),
        ),
    ]
