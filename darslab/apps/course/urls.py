from django.urls import path
import apps.course.views as view


urlpatterns = [
    path('courses', view.courses, name='course')
]

