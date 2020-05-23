"""Workplan models"""

# Django
from django.db import models
from django.contrib.postgres.fields import ArrayField


# Models
from django.contrib.auth.models import User
from subjects.models import Subject


class Workplan(models.Model):
    """Workplan model"""

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)

    unit = models.TextField()
    gen_comp_develop = models.TextField()
    scheduled_sessions = models.IntegerField()
    real_sessions = models.IntegerField()
    unit_assess_session = models.IntegerField()
    real_assess_session = models.IntegerField()
    learning_activity = models.TextField()
    teaching_activity = models.TextField()
    generic_competences = models.TextField()
    reprobation = models.IntegerField()
    desertion = models.IntegerField()
    review_date = models.DateTimeField()
    observations = models.TextField()
    subtopics = ArrayField(models.TextField())
    practices = ArrayField(models.TextField())
    didactic_support = ArrayField(models.TextField())
    required_equipment = ArrayField(models.TextField())
    information_sources = ArrayField(models.TextField())

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return user id and subject id"""
        return f'{self.user}, {self.subject}'
