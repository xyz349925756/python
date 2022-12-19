#!/usr/bin/python3
# -*-coding:utf-8-*-
# Author: xyz34
# Filer: ser.py
# Time: 2022年12月18日
from rest_framework import serializers
from app01 import models


# 序列化数据库的表,经量使用ModelSerializer
class BookModelSerializer(serializers.ModelSerializer):
    # create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    # last_update = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    # publish = serializers.CharField(source='publish.name')
    class Meta:
        model = models.Book
        # fields = '__all__'
        # depth = 0
        # fields = ()
        fields = ('id', 'name', 'price', 'publish', 'publish_name', 'author', 'author_name')
        extra_kwargs = {
            'publish': {'write_only': True},
            'publish_name': {'read_only': True},
            'author': {'write_only': True},
            'author_name': {'read_only': True},
        }
