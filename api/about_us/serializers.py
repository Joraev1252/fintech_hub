from rest_framework import serializers
from apps.about_us.models.about_us import AboutUsModel


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUsModel
        fields = "__all__"

