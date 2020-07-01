"""Subject views"""

# Api
from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

# Permissions
from rest_framework.permissions import IsAuthenticated
from subjects.permissions import IsOwner

# Models
from subjects.models import Subject
from grades.models import Grade

# Serializers
from subjects.serializers import ListStudentsSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_subjects_view(request):

    subjects = Subject.objects.filter(user=request.user)
    if not subjects:
        return Response(
            data={'detail': 'This user does not have subjects assigned'},
            status=status.HTTP_200_OK
        )

    data = {}
    for subject in subjects:
        data[subject.name] = subject.id

    return Response(
        data=data,
        status=status.HTTP_200_OK
    )


class ListGradesView(RetrieveAPIView):

    serializer_class = ListStudentsSerializer
    permission_classes = [
        IsAuthenticated,
        IsOwner
    ]
    queryset = Subject.objects.all()


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_score_view(request, **kwargs):
    """Updates the scores of the students"""
    data = request.data
    subject_id = kwargs['pk']
    
    if user_is_owner(subject_id, request.user):
        for student in data:
            try:

                grade = Grade.objects.get(
                    subject=subject_id,
                    student=student['no_ctrl']
                )
                grade.score = student['score']
                grade.save()

            except Grade.DoesNotExist:
                no_ctrl = student['no_ctrl']
                return Response(
                    data={'detail': f'The student {no_ctrl} does not exist'},
                    status=status.HTTP_404_NOT_FOUND
                )
    else:
        return Response(
            data={'detail': 'You must be the owner of this object'},
            status=status.HTTP_403_FORBIDDEN
        )
    return Response(status=status.HTTP_200_OK)
        

def user_is_owner(subject_id, user):
    """Cheks if the user is the owner of the object"""
    try:
        subject = Subject.objects.get(id=subject_id)
    except Subject.DoesNotExist:
        return False

    if user.id == subject.user.id:
        return True
    else: 
        return False