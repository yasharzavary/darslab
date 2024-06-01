from django.db import models

# Create your models here.
class Message(models.Model):
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    subject = models.CharField(max_length=40)
    mess = models.TextField()

    