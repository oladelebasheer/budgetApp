from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Project_list, name='list'),
    path('<slug:project_slug>', views.Project_detail, name='detail' )
]
