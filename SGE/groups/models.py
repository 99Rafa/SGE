"""Group models"""

# Django
from django.db import models


class Group(models.Model):
    """Group model"""

    semester = models.IntegerField()
    group = models.CharField(max_length=1)

    def __str__(self):
        """Returns semester and group"""
        return f'{self.semester}{self.group}'
