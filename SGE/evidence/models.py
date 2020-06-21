"""Evidence models"""

# Django
from django.db import models

# Models
from users.models import User
from subjects.models import Subject


class Evidence(models.Model):
    """Evidence model"""

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)

    title = models.TextField()
    file = models.TextField()
