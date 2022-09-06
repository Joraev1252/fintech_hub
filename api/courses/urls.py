from django.urls import path
from api.courses.views import *

app_name = 'courses'

urlpatterns = [
    path('', course_view, name='course'),
    path('fact/', fact_view, name='fact'),
    path('search/', search_view, name='search'),
]


