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

    unit = models.TextField(null=True, blank=True)
    gen_comp_develop = models.TextField(null=True, blank=True)
    scheduled_sessions = models.IntegerField(null=True)
    real_sessions = models.IntegerField(null=True)
    unit_assess_session = models.IntegerField(null=True)
    real_assess_session = models.IntegerField(null=True)
    learning_activity = models.TextField(null=True, blank=True)
    teaching_activity = models.TextField(null=True, blank=True)
    generic_competences = models.TextField(null=True, blank=True)
    reprobation = models.IntegerField(null=True)
    desertion = models.IntegerField(null=True)
    review_date = models.DateTimeField(null=True)
    observations = models.TextField(null=True, blank=True)
    subtopics = ArrayField(models.TextField(null=True, blank=True), null=True)
    practices = ArrayField(models.TextField(null=True, blank=True), null=True)
    didactic_support = ArrayField(models.TextField(null=True, blank=True), null=True)
    required_equipment = ArrayField(models.TextField(null=True, blank=True), null=True)
    information_sources = ArrayField(models.TextField(null=True, blank=True), null=True)

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
