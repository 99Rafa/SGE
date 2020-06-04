"""Student serializers"""

# APi
from rest_framework import serializers

# Models
from students.models import Student

class FullNameSerializer(serializers.RelatedField):
    """List the name of the students"""
    
    def to_representation(self, value):
        return value.full_name()