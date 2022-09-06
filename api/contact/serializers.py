from rest_framework import serializers
from apps.contact.models.contact import ContactModel


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactModel
        fields = [
                  'location',
                  'social_network1',
                  'social_network2',
                  'social_network3',
                  'social_network4',
                  'phone_number'
                  ]
