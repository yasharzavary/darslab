from django.urls import path
import apps.course.views as view


urlpatterns = [
    path('courses/', view.courses, name='courses'),
    path('course/<slug:slug_id>/', view.detail_course, name='detail_course'),
]

