from django.contrib import admin
from django.urls import path

from adminmodule import views, studentviews, parentviews

urlpatterns = [

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
    path('add_fee/', views.add_fee, name='add_fee'),
    path('view_fee/', views.view_fee, name='view_fee'),
    path('view_payment/', views.view_payment, name='view_payment'),
    path('add_notification/', views.add_notification, name='add_notification'),
    path('view_notification/', views.view_notification, name='view_notification'),
    path('view_attendance/', views.view_attendance, name='view_attendance'),
    path('add_attendance/', views.add_attendance, name='add_attendance'),
    path('add_staff/', views.add_staff, name='add_staff'),
    path('view_staff/', views.view_staff, name='view_staff'),
    path('update_staff/<int:id>/', views.update_staff, name='update_staff'),
    path('delete_staff/<int:id>/', views.delete_staff, name='delete_staff'),
    path('view_egrant_details/', views.view_egrant_details, name='view_egrant_details'),
    path('view_registration_details/', views.view_registration_details, name='view_registration_details'),
    path('approve_student/<int:id>/', views.approve_student, name='approve_student'),
    path('reject_student/<int:id>/', views.reject_student, name='reject_student'),
    path('approve_parent/<int:id>/', views.approve_parent, name='approve_parent'),
    path('reject_parent/<int:id>/', views.reject_parent, name='reject_parent'),

    path('student_page/', studentviews.student_page, name='student_page'),
    path('view_fee_student/', studentviews.view_fee, name='view_fee_student'),
    path('pay_fee/', studentviews.pay_fee, name='pay_fee'),
    path('view_attendance_student/', studentviews.view_attendance, name='view_attendance_student'),
    path('view_food_student/', studentviews.view_food_updates, name='view_food_student'),
    path('send_complaint/', studentviews.send_complaint, name='send_complaint'),
    path('view_send_compalints/', studentviews.view_send_compalints, name='view_send_compalints'),
    path('add_review/', studentviews.add_review, name='add_review'),
    path('notification_view_student/', studentviews.view_notification, name='notification_view_student'),


    path('parent_page/', parentviews.parent_page, name='parent_page'),
    path('hostel_details_parent/', parentviews.hostel_details, name='hostel_details_parent'),
    path('staff_details_parent/', parentviews.staff_details, name='staff_details_parent'),





]
