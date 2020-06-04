"""Subject models"""

# Django
from django.db import models

# Models
from users.models import User
from groups.models import Group
from students.models import Student


class Subject(models.Model):
    """Subject model"""

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    group = models.ForeignKey(Group, on_delete=models.DO_NOTHING)
    students = models.ManyToManyField(Student)

    name = models.CharField(max_length=50)
    no_units = models.IntegerField()
    theory_hours = models.IntegerField()
    practice_hours = models.IntegerField()
    credit = models.IntegerField(verbose_name='credits', db_column='credits')

    def __str__(self):
        """Returns subject name"""
        return f'{self.name}'
