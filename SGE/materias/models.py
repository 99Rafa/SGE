"""Modelo de materias"""

# Django
from django.db import models

# Modelos
from grupos.models import Grupo
from alumnos.models import Alumno


class Materia(models.Model):
    """Modelo de materias
    
    Relacion muchos a muchos con alumnos
    Relacion muchos a uno con grupos
    """

    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    alumnos = models.ManyToManyField(Alumno)

    nombre_materia = models.CharField(max_length=30)
    no_unidades = models.IntegerField()
    hrs_teoria = models.IntegerField()
    hrs_practica = models.IntegerField()
    creditos = models.IntegerField()