"""User views"""

# Django
from django.shortcuts import get_object_or_404

# Api
from rest_framework.generics import RetrieveUpdateAPIView
from djoser.conf import settings

# Permissions
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner

# Models
from users.models import User

# Serializers
from users.serializers import ProfileSerializer


class UserDetailView(RetrieveUpdateAPIView):
    """User detail view"""
    permission_classes = [IsAuthenticated]

    serializer_class = ProfileSerializer
    queryset = User.objects.all()

    def get_queryset(self):
        qs = User.objects.all()
        logged_in_user = qs.filter(id=self.request.user.id)
        return logged_in_user

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, id=self.request.user.id)
        return obj