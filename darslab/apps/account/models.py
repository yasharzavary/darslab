from django.db import models
from apps.course.models import Course

class Profile(models.Model):
    class Meta:
        db_table = 'profile'
        verbose_name = 'پروقایل'
        verbose_name_plural = 'پروفایل‌ها'
    name = models.CharField(max_length=30, verbose_name='نام')
    family = models.CharField(max_length=40, verbose_name='نام خانوادگی')
    password = models.CharField(max_length=30, verbose_name='رمز عبور')
    phone_number = models.CharField(max_length=11, verbose_name='شماره تلفن', primary_key=True)
    email = models.CharField(max_length=50, verbose_name='ایمیل', blank=True)
    age = models.IntegerField(verbose_name='سن')
    CERTIFICATES = [
        ('diploma', 'دیپلم'),
        ('bachelor', 'کارشناسی'),
        ('master', 'ارشد'),
        ('phd', 'دکترا'),
    ]
    certificate = models.CharField(choices=CERTIFICATES, max_length=15, verbose_name='تحصیلات')
    profile_image = models.CharField(max_length=20, default='nophoto.png', verbose_name='عکس')
    slug = models.models.SlugField()
    courses = models.ManyToManyField(Course, verbose_name='دوره‌ها')
    active = models.BooleanField(default=False)

