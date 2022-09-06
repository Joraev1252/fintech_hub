from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from api.partners.serializers import *
from apps.partners.models.partners import PartnersModel
from apps.partners.models.registration import RegistrationModel


@api_view(['GET', ])
def partners_view(request):
    partners = PartnersModel.objects.all()
    serializer = PartnersSerializer(partners, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def post_data(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = "Data has been sent!"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

