from django.urls import path
from . import views

urlpattens = [path('', views.post_list, name='post_list')]