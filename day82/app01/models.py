from django.db import models


# Create your models here.

class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    repeat_password = models.CharField(max_length=32)
    email = models.EmailField(max_length=32)
    gender_choices = (
        (1, 'male'),
        (2, 'woman'),
        (3, 'other')
    )
    gender = models.IntegerField(choices=gender_choices)
