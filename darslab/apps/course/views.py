from django.shortcuts import render
from apps.course.models import Course


def courses(req):
    courses = Course.objects.all()
    context = {
        'course': courses,
    }
    return render(req, 'course/cors.html', context)

