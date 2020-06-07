"""User views"""

# Api
from rest_framework.generics import RetrieveUpdateAPIView

# Permissions
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner

# Models
from users.models import User

# Serializers
from users.serializers import ProfileSerializer


class UserDetailView(RetrieveUpdateAPIView):
    """User detail view"""

    serializer_class = ProfileSerializer
    permission_classes = [
        IsAuthenticated,
        IsOwner
    ]

    lookup_field = 'username'
    lookup_url_kwarg = 'username'
    queryset = User.objects.all()
