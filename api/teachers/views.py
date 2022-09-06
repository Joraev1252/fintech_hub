from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from apps.teachers.models.teachers import TeacherModel
from apps.teachers.models.comments import CommentsModel
from api.teachers.serializers import TeacherSerializer, CommentSerializer


@api_view(['GET', ])
def teacher_view(request):
    teacher = TeacherModel.objects.all()
    serializer = TeacherSerializer(teacher, many=True)
    return Response(serializer.data)


@api_view(['GET', ])
def comment_view(request):
    comment = CommentsModel.objects.all()
    serializer = CommentSerializer(comment, many=True)
    return Response(serializer.data)
