from django.db import models

class Course(models.Model):
    class Meta:
        db_table = 'course'
        verbose_name = 'دوره'
        verbose_name_plural = 'دوره‌ها'
    title = models.CharField(max_length=30, verbose_name='عنوان')
    price = models.IntegerField(verbose_name='قیمت')
    teacher = models.CharField(max_length=40, verbose_name='مدرس')
    description = models.TextField( verbose_name='توضیحات')
    time = models.IntegerField( verbose_name='مدت زمان')
    SCORES = [
        ('1', '۱'),
        ('2', '۲'),
        ('3', '۳'),
        ('4', '۴'),
        ('5', '۵'),
    ]
    score = models.CharField(choices=SCORES, max_length=20, verbose_name='امتیاز')
    LEVELS = [
        ('beginner', 'مقدمات'),
        ('intermediate', 'متوسط'),
        ('professional', 'پیشرفته'),
    ]
    level = models.CharField(choices=LEVELS, max_length=20, verbose_name='سطح')
    class_number = models.IntegerField( verbose_name='تعداد جلسات')
    image_path = models.CharField(max_length=30, verbose_name='آدرس عکس')
    
