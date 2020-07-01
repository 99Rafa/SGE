"""Work plan views"""

# Api 
from rest_framework.generics import (
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView
)

# Permissions
from rest_framework.permissions import IsAuthenticated
from work_plans.permissions import IsOwnerOfSubject, IsOwnerOfWorkplan

# Models
from work_plans.models import Workplan, RequiredVisit

# Serializers
from work_plans.serializers import (
    DetailWorkPlanSerializer,
    ListWorkPlanSerializer
)


class CreateWorkplanView(CreateAPIView):

    serializer_class = DetailWorkPlanSerializer
    permission_classes = [IsAuthenticated]
    queryset = Workplan.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ListWorkPlanView(ListAPIView):

    serializer_class = ListWorkPlanSerializer
    permission_classes = [
        IsAuthenticated,
        IsOwnerOfSubject
    ]

    def get_queryset(self):
        subject_id = self.kwargs['pk']
        return Workplan.objects.filter(subject=subject_id)


class DetailWorkPlanView(RetrieveUpdateDestroyAPIView):
    
    serializer_class = DetailWorkPlanSerializer
    permission_classes = [
        IsAuthenticated,
        IsOwnerOfWorkplan
    ]
    queryset = Workplan.objects.all()
