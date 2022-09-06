from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from api.about_us.serializers import AboutSerializer
from apps.about_us.models.about_us import AboutUsModel


@api_view(['GET', ])
def about_us_view(request):
    about = AboutUsModel.objects.all()
    serializer = AboutSerializer(about, many=True)
    return Response(serializer.data)

