from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    password = models.CharField(max_length=30)
    email = models.EmailField()         
    

class Nota(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.TextField()
    urgencia = models.IntegerField()
    user_id = models.IntegerField()

    

