from rest_framework import serializers

from apps.teachers.models.teachers import TeacherModel
from apps.teachers.models.comments import CommentsModel


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherModel
        fields = [
                 'image',
                 'teacher',
                 'course',
                 'about',
                 'experience',
                 'social_network1',
                 'social_network2',
                 'social_network3',
                 'social_network4'
                  ]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentsModel
        fields = [
            'title',
            'body',
            'author_image',
            'author_name',
            'author_speciality'
        ]
