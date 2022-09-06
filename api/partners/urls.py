from django.urls import path
from api.partners.views import *

app_name = 'partners'

urlpatterns = [
    path('', partners_view, name='partners'),
    path('post/', post_data, name='post'),
]


