"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import app01.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', app01.views.index),
    path('static/', app01.views.static),
    path('login/', app01.views.login),
    path('ab_render/',app01.views.ab_render),
    path('reg/',app01.views.reg),
    path('userlist/',app01.views.userlist),
    path('edit_user/',app01.views.edit_user),
    path('delete_user/',app01.views.delete_user),
]
