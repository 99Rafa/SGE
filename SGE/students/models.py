"""Student models"""

# Django
from django.db import models


class Student(models.Model):
    """Student model"""

    no_ctrl = models.CharField(max_length=12, primary_key=True, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        """Return control number"""
        return f'{self.no_ctrl}'

    def full_name(self):
        """Returns the full name of the student"""
        return f'{self.last_name} {self.first_name}'