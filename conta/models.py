from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    primeiro_nome = models.CharField(max_length=30)
    ultimo_nome = models.CharField(max_length=30)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    endereco = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username

