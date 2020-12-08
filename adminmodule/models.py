
from django.db import models
from django.utils import timezone

from accounts.models import Parent,Student


class HostelDetails(models.Model):
    total_rooms = models.CharField(max_length=100)
    occupied = models.CharField(max_length=100)
    annual_expenses = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=10)

# class BookRoom(models.Model):
#     name = models.ForeignKey(UserRegister,on_delete=models.CASCADE)
#

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
    complaint = models.TextField(max_length=100)


class Payment(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    payment = models.CharField(max_length=100)
    e_grant = models.CharField(max_length=100)


class Fees(models.Model):
    name = models.ForeignKey(Student, on_delete=models.CASCADE)
    accommodation = models.CharField(max_length=100)
    water = models.CharField(max_length=100)
    electricity = models.CharField(max_length=100)
    caution_deposit = models.CharField(max_length=100)
    security = models.CharField(max_length=100)
    mess = models.CharField(max_length=100)
    others = models.CharField(max_length=100)


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



class Review(models.Model):
    name = models.CharField(max_length=50)
    review = models.TextField(max_length=200)

