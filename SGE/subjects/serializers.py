"""Subject serializers"""

# APi
from rest_framework import serializers

# Models
from subjects.models import Subject

# Serializers
from grades.serializers import ListGradesSerializer

class ListStudentsSerializer(serializers.ModelSerializer):
    """List the name of the subjects"""
    grades = ListGradesSerializer(many=True)

    class Meta:
        model = Subject
        fields = ['id', 'name', 'grades']
