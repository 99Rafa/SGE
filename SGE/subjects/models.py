"""Subject models"""

# Django
from django.db import models

# Models
from groups.models import Group


class Subject(models.Model):
    """Subject model"""

    id_group = models.ForeignKey(Group, on_delete=models.DO_NOTHING)

    name = models.CharField(max_length=50)
    no_units = models.IntegerField()
    theory_hours = models.IntegerField()
    practice_hours = models.IntegerField()
    credit = models.IntegerField(verbose_name='credits')

    def __str__(self):
        """Returns subject name"""
        return f'{self.name}'
