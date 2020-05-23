"""Workplan models"""

# Django
from django.db import models
from django.contrib.postgres.fields import ArrayField


# Models
from django.contrib.auth.models import User
from subjects.models import Subject


class Workplan(models.Model):
    """Workplan model"""

    id_user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    id_subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)

    unit = models.IntegerField()
    gen_comp_develop = models.CharField()
    scheduled_sessions = models.IntegerField()
    real_sessions = models.IntegerField()
    unit_assess_session = models.IntegerField()
    real_assess_session = models.IntegerField()
    learning_activity = models.CharField()
    teaching_activity = models.CharField()
    generic_competences = models.CharField()
    reprobation = models.IntegerField()
    desertion = models.IntegerField()
    review_date = models.DateTimeField()
    observations = models.CharField()
    subtopics = ArrayField(models.CharField())
    practices = ArrayField(models.CharField())
    didactic_support = ArrayField(models.CharField())
    required_equipment = ArrayField(models.CharField())
    information_sources = ArrayField(models.CharField())

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return user id and subject id"""
        return f'{self.id_user}, {self.id_subject}'
