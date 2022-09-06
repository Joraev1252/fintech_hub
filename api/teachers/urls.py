from django.urls import path
from api.teachers.views import *

app_name = 'teacher'

urlpatterns = [
    path('', teacher_view, name='teacher'),
    path('comment/', comment_view, name='comment')
]


