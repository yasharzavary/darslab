from django.shortcuts import render
from apps.course.models import Course
from django.conf import settings


def courses(req):
    courses = Course.objects.all()
    context = {
        'media_url': settings.MEDIA_URL,
        'course': courses,
    }
    return render(req, 'course/cors.html', context)



def detail_course(req, slug_id):
    course = Course.objects.filter(slug = slug_id)
    return render(req, 'course/course.html', {'course': course})
