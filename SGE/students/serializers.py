"""Student serializers"""

# APi
from rest_framework import serializers

# Models
from students.models import Student

class FullNameSerializer(serializers.ModelSerializer):
    """List the no ctrl and the full name of the student"""
    
    class Meta:
        model = Student
        fields = ['no_ctrl', 'full_name']