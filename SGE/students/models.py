"""Student models"""

# Django
from django.db import models


class Student(models.Model):
    """Student model"""

    no_ctrl = models.CharField(max_length=12)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        """Return control number"""
        return f'{self.no_ctrl}'
