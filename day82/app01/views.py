from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from app01.models import UserInfo
from app01.ser_api import UserinfoSerializer


class User1View(ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserinfoSerializer

    @action(methods=['get', 'post'], detail=False)
    def get_l(self, request, pk):
        print(pk)
        user_list = self.get_queryset()[:10]  # error 'Manager' object is not subscriptable queryset 后面需要加.all()
        ser = self.get_serializer(user_list, many=True)
        return Response(ser.data)
