from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from apps.contact.models.contact import ContactModel
from api.contact.serializers import ContactSerializer


@api_view(['GET', ])
def contact_view(request):
    contact = ContactModel.objects.all()
    serializer = ContactSerializer(contact, many=True)
    return Response(serializer.data)


