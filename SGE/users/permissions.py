"""User permissions"""

# Api
from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):

    message = 'You must be the owner of this object.'
    
    def has_object_permission(self, request, view, obj):
        """Check if the user is the owner"""
        return request.user == obj