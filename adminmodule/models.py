from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_parent = models.BooleanField(default=False)


class AdminRegister(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    phone_no = models.CharField(max_length=10,null=True)

class HostelDetails(models.Model):
    total_rooms = models.CharField(max_length=100)
    occupied = models.CharField(max_length=100)
    annual_expenses = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=100)


class Food(models.Model):
    breakfast = models.CharField(max_length=100)
    lunch = models.CharField(max_length=100)
    dinner = models.CharField(max_length=100)

class Income(models.Model):
    received = models.CharField(max_length=100)
    given = models.CharField(max_length=100)
    total_income = models.CharField(max_length=100)


class Complaint(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    complaint = models.CharField(max_length=100)


class Payment(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    payment = models.CharField(max_length=100)
    e_grant = models.CharField(max_length=100)


class Notification(models.Model):
    to = models.CharField(max_length=100)
    notification = models.TextField(max_length=100)
    time = models.TimeField()


class Attendance(models.Model):
    name = models.CharField(max_length=100)
    initial_day = models.DateField()
    final_day = models.DateField()
    percentage = models.CharField(max_length=100)

class StaffRegister(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=10)
    email = models.EmailField()
    address = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)






