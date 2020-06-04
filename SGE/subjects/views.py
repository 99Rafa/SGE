"""Subject views"""

# Api
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

# Permissions
from rest_framework.permissions import IsAuthenticated

# Models
from subjects.models import Subject


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_subjects_view(request):

    subjects = Subject.objects.filter(user=request.user)
    if not subjects:
        return Response(
            data={
                'detail': 'This user does not have subjects assigned'
            },
            status=status.HTTP_200_OK
        )

    data = {}
    for subject in subjects:
        data[subject.name] = subject.id

    return Response(
        data=data,
        status=status.HTTP_200_OK
    )
