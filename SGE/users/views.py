"""User views"""

# Api
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

# Models
from users.models import User

# Serializers
from users.serializers import ProfileSerializer


class UserDetailView(RetrieveAPIView):
    """User detail view"""

    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    lookup_field = 'username'
    lookup_url_kwarg = 'username'
    queryset = User.objects.all()
