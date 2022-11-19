from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import ModelViewSet
from .models import Book
from app01.apis.books_api import BookModelSerializer,StudentSerializer

from django.views import View
from rest_framework.views import APIView
from rest_framework.request import Request

class BooksViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer

from .models import Student
class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer