"""Evidence serializers"""

# Api
from rest_framework import serializers

# Models
from evidence.models import Evidence


class EvidenceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Evidence
        fields = ['id', 'subject', 'title', 'file']
