"""Grades serializers"""

# APi
from rest_framework import serializers

# Models
from grades.models import Grade

from students.serializers import FullNameSerializer

class ListGradesSerializer(serializers.ModelSerializer):
    """list the student with score"""
    student = FullNameSerializer(read_only=True, many=False)
    
    class Meta:
        model = Grade
        fields = ['student', 'score']