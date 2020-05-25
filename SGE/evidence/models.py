"""Evidence models"""

# Django
from django.db import models

# Models
from django.contrib.auth.models import User
from subjects.models import Subject


class Evidence(models.Model):
    """Evidence model"""

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)

    file = models.BinaryField()
