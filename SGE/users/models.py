"""User proxy model"""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Profile model

    Proxy model that extends the base data with other information
    """

    profile_picture = models.BinaryField(null=True)
    department = models.CharField(max_length=100)
