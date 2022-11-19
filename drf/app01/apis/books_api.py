from rest_framework.serializers import ModelSerializer
from app01.models import Book,Student


class BookModelSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"