"""Qualification models"""

# Django
from django.db import models
from django.core.validators import MaxValueValidator

# Models
from django.contrib.auth.models import User
from students.models import Student
from subjects.models import Subject


class Qualification(models.Model):
    """Qualification model"""

    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    no_ctrl_student = models.ForeignKey(Student, on_delete=models.DO_NOTHING,)

    score1 = models.IntegerField(validators=[MaxValueValidator(100)])
    score2 = models.IntegerField(validators=[MaxValueValidator(100)])
    score3 = models.IntegerField(validators=[MaxValueValidator(100)])
    score4 = models.IntegerField(validators=[MaxValueValidator(100)])
    score5 = models.IntegerField(validators=[MaxValueValidator(100)])
    score6 = models.IntegerField(validators=[MaxValueValidator(100)])
    final_score = models.FloatField()

    def __str__(self):
        """Return control number and subject id"""
        return f'{self.no_ctrl_student}, {self.subject}'
