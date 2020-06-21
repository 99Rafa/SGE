"""Evicence views"""

# Api
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# Permissions
from rest_framework.permissions import IsAuthenticated

# Modoels
from evidence.models import Evidence

# Serializers
from evidence.serializers import EvidenceSerializer


class EvidenceView(ListCreateAPIView):

    serializer_class = EvidenceSerializer
    permission_classes = [IsAuthenticated]
    queryset = Evidence.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DetailEvideceView(RetrieveUpdateDestroyAPIView):

    serializer_class = EvidenceSerializer
    permission_classes = [IsAuthenticated]
    queryset = Evidence.objects.all()
