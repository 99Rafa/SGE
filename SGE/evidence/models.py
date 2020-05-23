"""Evidence models"""

# Django
from django.db import models

# Models
from django.contrib.auth.models import User


class Evidence(models.Model):
    """Evidence model"""

    id_user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    file = models.BinaryField()