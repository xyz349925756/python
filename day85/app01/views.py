from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView

from rest_framework.response import Response

from app01.ser import BookModelSerializer
from app01 import models

class BookAPIView(APIView):

    def get(self,request,*args,**kwargs):
        # print(kwargs)  #{'pk': '1'}
        if kwargs:
            print('1')
            book_list = models.Book.objects.filter(is_delete=False).filter(id=kwargs['pk']).first()
            book_list_ser = BookModelSerializer(book_list)
            return Response(data=book_list_ser.data)

        else:
            print('2')
            book_list = models.Book.objects.all().filter(is_delete=False)  # 过滤没有标记is_delete的field
            book_list_ser = BookModelSerializer(book_list,many=True)
            return Response(data=book_list_ser.data)