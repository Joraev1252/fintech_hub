from django.urls import path
from api.contact.views import *

app_name = 'contact'

urlpatterns = [
    path('', contact_view, name='contact'),
]


