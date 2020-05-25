"""User proxy model"""

# Django
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """Profile model

    Proxy model that extends the base data with other information
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    profile_picture = models.BinaryField()
    department = models.CharField(max_length=100)
