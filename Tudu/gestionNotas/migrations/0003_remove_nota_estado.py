# Generated by Django 4.2.7 on 2023-12-18 03:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestionNotas', '0002_nota_titulo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nota',
            name='estado',
        ),
    ]
