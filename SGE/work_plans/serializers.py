"""Work plan serializers"""

# Api
from rest_framework import serializers

# Models
from work_plans.models import Workplan, RequiredVisit


class RequiredVisitSerializer(serializers.ModelSerializer):
    """Required visit serializer"""

    class Meta:
        model = RequiredVisit
        fields = ['id', 'workplan', 'date', 'destination']


class ListWorkPlanSerializer(serializers.ModelSerializer):
    """Serializer used to list few information from the workplan"""

    class Meta:
        model = Workplan
        fields = [
            'id',
            'subject',
            'unit',
        ]


class DetailWorkPlanSerializer(serializers.ModelSerializer):
    """Work plan serializer"""

    class Meta:
        model = Workplan
        fields = [
            'subject',
            'unit',
            'gen_comp_develop',
            'scheduled_sessions',
            'real_sessions',
            'unit_assess_session',
            'real_assess_session',
            'learning_activity',
            'teaching_activity',
            'generic_competences',
            'reprobation',
            'desertion',
            'review_date',
            'observations',
            'subtopics',
            'practices',
            'didactic_support',
            'required_equipment',
            'information_sources',
        ]