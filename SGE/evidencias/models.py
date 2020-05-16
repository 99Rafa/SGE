"""Modelo de evidencias"""

# Django
from django.db import models
from django.contrib.auth.models import User


class Evidencia(models.Model):
    """Modelo de evidencias

    Modelo que se relaciona de muchos a uno con User
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    archivo = models.FileField()

    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)