from django.contrib import admin
from django.urls import path

from adminmodule import views

urlpatterns = [
    path('admin_register/', views.admin_register, name='admin_register'),
    path('', views.login_view, name='login_view'),
    path('logout_view/', views.logout_view, name='logout_view'),
    path('admin_page/', views.admin_page, name='admin_page'),

    path('add_hostel_detail/', views.add_hostel_detail, name='add_hostel_detail'),
    path('view_hostel_detail/', views.view_hostel_detail, name='view_hostel_detail'),
    path('update_hostel_detail/<int:id>/', views.update_hostel_detail, name='update_hostel_detail'),
    path('delete_hostel_detail/<int:id>/', views.delete_hostel_detail, name='delete_hostel_detail'),

    path('add_food_detail/', views.add_food_detail, name='add_food_detail'),
    path('view_food_detail/', views.view_food_detail, name='view_food_detail'),
    path('update_food_detail/<int:id>/', views.update_food_detail, name='update_food_detail'),
    path('delete_food_detail/<int:id>/', views.delete_food_detail, name='delete_food_detail'),

    path('add_income_detail/', views.add_income_detail, name='add_income_detail'),
    path('view_income_detail/', views.view_income_detail, name='view_income_detail'),
    path('view_complaint/', views.view_complaint, name='view_complaint'),
    path('view_payment/', views.view_payment, name='view_payment'),
    path('add_notification/', views.add_notification, name='add_notification'),
    path('view_notification/', views.view_notification, name='view_notification'),
    path('view_attendance/', views.view_attendance, name='view_attendance'),
    path('add_staff/', views.add_staff, name='add_staff'),
    path('view_staff/', views.view_staff, name='view_staff'),
    path('update_staff/<int:id>/', views.update_staff, name='update_staff'),
    path('delete_staff/<int:id>/', views.delete_staff, name='delete_staff'),
    path('view_egrant_details/', views.view_egrant_details, name='view_egrant_details'),
    path('view_registration_details/', views.view_registration_details, name='view_registration_details'),

    path('index/', views.index)

]
