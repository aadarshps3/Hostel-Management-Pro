from django.contrib import admin
from django.urls import path

from adminmodule import views

urlpatterns = [
    path('admin_register/', views.admin_register, name='admin_register'),






]
