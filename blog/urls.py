from django.urls import path
from django.contrib import admin
from django.conf.urls import include
from django.conf.urls import url, include
from . import views
from django.conf.urls import include
from django.urls import include, path


urlpatterns = [
    path('', views.post_list, name='post_list'),
]
