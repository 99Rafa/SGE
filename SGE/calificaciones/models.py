"""Modelo de calificaciones"""

# Django
from django.db import models
from django.core.validators import MaxValueValidator

# Modelos
from django.contrib.auth.models import User
from materias.models import Materia
from alumnos.models import Alumno


class Calificaciones(models.Model):
    """Modelo de calificaciones
    
    Relacion muchos a uno con User
    Relacion muchos a uno con materias
    Relacion muchos a uno con materias
    """

    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    materia = models.ForeignKey(Materia, on_delete=models.DO_NOTHING)
    NoCtrlAlumno = models.ForeignKey(Alumno, on_delete=models.DO_NOTHING)

    
    cal1 = models.IntegerField(validators=[MaxValueValidator(100)])
    cal2 = models.IntegerField(validators=[MaxValueValidator(100)])
    cal3 = models.IntegerField(validators=[MaxValueValidator(100)])
    cal4 = models.IntegerField(validators=[MaxValueValidator(100)])
    cal5 = models.IntegerField(validators=[MaxValueValidator(100)])
    cal6 = models.IntegerField(validators=[MaxValueValidator(100)])
    cal7 = models.IntegerField(validators=[MaxValueValidator(100)])

    cal_final = models.IntegerField(validators=[MaxValueValidator(100)])
