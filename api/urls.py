from django.urls import path, include


app_name = 'api'

urlpatterns = [
    path("about_us/", include("api.about_us.urls")),
    path("contact/", include("api.contact.urls")),
    path("courses/", include("api.courses.urls")),
    # path("courses/", include("api.courses.urls")),
    path("partners/", include("api.partners.urls")),
    path("teacher/", include("api.teachers.urls"))
]

