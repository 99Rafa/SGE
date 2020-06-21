"""Evidence permissions"""

# Api
from rest_framework.permissions import BasePermission

# Models
from subjects.models import Subject


class IsOwnerOfSubject(BasePermission):

    def has_permission(self, request, view):
        """Checks if the user has permission over the subject"""

        try:
            subject_id = view.kwargs['pk']
            subject = Subject.objects.get(id=subject_id)

            if request.user == subject.user:
                return True
            else:
                return False

        except Subject.DoesNotExist:
            return False


class IsOwnerOfEvidence(BasePermission):

    def has_object_permission(self, request, view, obj):
        """Cheks if the user is the owner of the Evidence"""
        if request.user == obj.user:
            return True
        else:
            return False
