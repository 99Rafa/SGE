"""Modelo de grupos"""

# Django
from django.db import models


class Grupo(models.Model):

    semestre = models.IntegerField()
    grupo = models.CharField(max_length=3)