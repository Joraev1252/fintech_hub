from django.urls import path
from api.courses.views import *

app_name = 'courses'

urlpatterns = [
    path('', course_view, name='course'),
    path('courses/<int:pk>/', course_detail_view, name='course_detail'),
    path('fact/', fact_view, name='fact'),
    path('search/', search_view, name='search'),

]


