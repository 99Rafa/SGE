"""Workplan models"""

# Django
from django.db import models
from django.contrib.postgres.fields import ArrayField


# Models
from users.models import User
from subjects.models import Subject


class Workplan(models.Model):
    """Workplan model"""

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    subject = models.ForeignKey(Subject, related_name='workplans', on_delete=models.DO_NOTHING)

    unit = models.TextField()
    gen_comp_develop = models.TextField()
    scheduled_sessions = models.IntegerField(null=True)
    real_sessions = models.IntegerField(null=True)
    unit_assess_session = models.IntegerField(null=True)
    real_assess_session = models.IntegerField(null=True)
    learning_activity = models.TextField()
    teaching_activity = models.TextField()
    generic_competences = models.TextField()
    reprobation = models.IntegerField(null=True)
    desertion = models.IntegerField(null=True)
    review_date = models.DateTimeField(null=True)
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


class RequiredVisit(models.Model):
    """Required visit model"""

    workplan = models.ForeignKey(Workplan, on_delete=models.CASCADE)

    date = models.DateTimeField()
    destination = models.CharField(max_length=100)
