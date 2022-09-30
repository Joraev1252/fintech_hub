from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from django.db.models import Q
from rest_framework import filters

from api.courses.serializers import CourseSerializer, FactsSerializer, SearchSerializer
from api.teachers.serializers import TeacherSerializer
from apps.courses.models.courses import CourseModel
from apps.courses.models.facts import FactsModel
from apps.teachers.models.teachers import TeacherModel


@api_view(['GET', ])
def course_view(request):
    course = CourseModel.objects.all()
    serializer = CourseSerializer(course, many=True)
    return Response(serializer.data)


def course_detail_view(request, pk):
    course = CourseModel.objects.get(id=pk)
    serializer = CourseSerializer(course)
    return Response(serializer.data)
@api_view(['GET', ])
def fact_view(request):
    fact = FactsModel.objects.all()
    serializer = FactsSerializer(fact, many=True)
    return Response(serializer.data)


@api_view(['POST', ])
def search_view(request):
    a = request.data['word']
    print(request.data)
    if request.method == 'POST':
        queryset_news = CourseModel.objects.filter(
            Q(course__icontains=a))

        # queryset_tenders = TeacherModel.objects.all()
        queryset_tenders = TeacherModel.objects.filter(
            Q(teacher__icontains=a))

        serializer_courses = CourseSerializer(queryset_news, many=True)
        serializer_teacher = TeacherSerializer(queryset_tenders, many=True)
        new_data = {
            "found_courses": serializer_courses.data,
            "found_speakers": serializer_teacher.data
        }

        return Response(new_data)
