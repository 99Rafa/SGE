"""Modelo de planes de trabajo"""

# Django
from django.db import models

# Modelos
from django.contrib.auth.models import User
from materias.models import Materia


class PlanTrabajo(models.Model):
    """Modelo de plan de trabajo

    Relacion muchos a uno con User
    Relacion muchos a uno con materias
    """

    verbose_name = 'plan trabajo'
    verbose_name_plural = ''

    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    materia = models.ForeignKey(Materia, on_delete=models.DO_NOTHING)

    unidad = models.IntegerField(null=True)
    comp_gen_a_desarrollar = models.CharField(max_length=500, blank=True)
    sesiones_programadas = models.IntegerField(null=True)
    sesiones_reales = models.IntegerField(null=True)
    sesion_real_evaluacion = models.IntegerField(null=True)
    actividad_aprendizaje = models.CharField(max_length=500, blank=True)
    actividad_ensenanza = models.CharField(max_length=500, blank=True)
    competencias_genericas = models.CharField(max_length=500, blank=True)
    reprobacion = models.IntegerField(null=True)
    desercion = models.IntegerField(null=True)
    fercha_revision = models.DateField()
    observaciones = models.CharField(max_length=500, blank=True)

    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)


class Subema(models.Model):
    """Modelo de subtema

    Relacion muchos a uno con plan de trabajo
    """
    
    plan_trabajo = models.ForeignKey(PlanTrabajo, on_delete=models.CASCADE)
    contenido = models.CharField(max_length=500, blank=True)


class VisitaRequerida(models.Model):
    """Modelo de visitas requeridas

    Relacion muchos a uno con plan de trabajo
    """
    
    plan_trabajo = models.ForeignKey(PlanTrabajo, on_delete=models.CASCADE)
    fecha = models.DateField()
    destino = models.CharField(max_length=200)


class Practica(models.Model):
    """Modelo de practicas

    Relacion muchos a uno con plan de trabajo
    """
    
    plan_trabajo = models.ForeignKey(PlanTrabajo, on_delete=models.CASCADE)
    contenido = models.CharField(max_length=500, blank=True)


class ApoyoDidactico(models.Model):
    """Modelo de apoyo didactico

    Relacion muchos a uno con plan de trabajo
    """
    
    plan_trabajo = models.ForeignKey(PlanTrabajo, on_delete=models.CASCADE)
    contenido = models.CharField(max_length=500, blank=True)


class EquipoRequerido(models.Model):
    """Modelo de Equipo requerido

    Relacion muchos a uno con plan de trabajo
    """
    
    plan_trabajo = models.ForeignKey(PlanTrabajo, on_delete=models.CASCADE)
    contenido = models.CharField(max_length=500, blank=True)


class FuenteInformacion(models.Model):
    """Modelo de fuentes de informacion

    Relacion muchos a uno con plan de trabajo
    """
    
    plan_trabajo = models.ForeignKey(PlanTrabajo, on_delete=models.CASCADE)
    contenido = models.CharField(max_length=500, blank=True)