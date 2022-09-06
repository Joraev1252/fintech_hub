from rest_framework import serializers
from apps.courses.models.courses import CourseModel
from apps.courses.models.facts import FactsModel


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseModel
        fields = [
                  'image',
                  'teacher_image',
                  'teacher',
                  'course',
                  'rating',
                  'price',
                  'lessons_amount',
                  'teacher_level',
                  'lesson_duration'
                  ]


class FactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactsModel
        fields = [
                  'image',
                  'title',
                  'subtitle',
                  'graduates',
                  'employment',
                  'salary',
                  'video'
                  ]


class SearchSerializer(serializers.Serializer):
    word = serializers.CharField(max_length=255)
    class Meta:
        fields = "__all__"