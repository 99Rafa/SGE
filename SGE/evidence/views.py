"""Evicence views"""

# Api
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView
)
# Permissions
from rest_framework.permissions import IsAuthenticated
from evidence.permissions import IsOwnerOfSubject, IsOwnerOfEvidence

# Modoels
from evidence.models import Evidence

# Serializers
from evidence.serializers import EvidenceSerializer


class CreateEvidenceView(CreateAPIView):

    serializer_class = EvidenceSerializer
    permission_classes = [IsAuthenticated]
    queryset = Evidence.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ListEvidenceView(ListAPIView):

    serializer_class = EvidenceSerializer
    permission_classes = [
        IsAuthenticated,
        IsOwnerOfSubject
    ]
    queryset = Evidence.objects.all()

    def get_queryset(self):
        evidence_id = self.kwargs['pk']
        return Evidence.objects.filter(subject=evidence_id)


class DetailEvideceView(RetrieveUpdateDestroyAPIView):

    serializer_class = EvidenceSerializer
    permission_classes = [
        IsAuthenticated,
        IsOwnerOfEvidence
    ]
    queryset = Evidence.objects.all()
