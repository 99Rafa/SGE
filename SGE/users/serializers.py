"""User serializers"""

# Api
from rest_framework import serializers

# Models
from users.models import User


class ProfileSerializer(serializers.ModelSerializer):
    """Profile serializer"""

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'department')