from rest_framework import serializers
from apps.partners.models.partners import PartnersModel
from apps.partners.models.registration import RegistrationModel


class PartnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnersModel
        fields = ['image']


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrationModel
        fields = [
            'full_name',
            'phone_number',
            'text'
        ]