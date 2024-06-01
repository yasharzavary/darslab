from django.contrib import admin
from apps.course.models import Course


@admin.register(Course)
class courseAdmin(admin.ModelAdmin):
    list_display = ('title', 'teacher', 'score', 'level')
    list_filter = ('teacher', 'level', 'score', 'price')
    search_fields = ('teacher', 'title')
    prepopulated_fields = {
        'slug': ('title', 'teacher'),
    }


