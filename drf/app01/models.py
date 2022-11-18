from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=64,verbose_name='BookName')
    publishing = models.CharField(max_length=64,verbose_name='Publishing Company')
    price = models.DecimalField(max_digits=5,decimal_places=2)
    author = models.CharField(max_length=32)
