from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=64,verbose_name='BookName')
    publishing = models.CharField(max_length=64,verbose_name='Publishing Company')
    price = models.DecimalField(max_digits=5,decimal_places=2)
    author = models.CharField(max_length=32)


class Student(models.Model):
    name = models.CharField(max_length=32,verbose_name="姓名")
    age = models.IntegerField(verbose_name="年龄")
    score_choices = {
        (1,'A'),
        (2,'B'),
        (3,'C'),
        (4,'D'),
        (5,'E')
    }
    score = models.IntegerField(choices=score_choices)
