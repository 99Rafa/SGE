"""Modelo de alumnos"""

# Django
from django.db import models


class Alumno(models.Model):
    """Modelo de alumnos"""

    NoCtrl = models.CharField(max_length=15, primary_key=True, editable=False)
    nombre = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=20)
    semestre = models.IntegerField()