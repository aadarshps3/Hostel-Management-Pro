from django.db import models
from django.utils import timezone
from accounts.models import Parent, Student


class HostelDetails(models.Model):
    total_rooms = models.CharField(max_length=100)
    occupied = models.CharField(max_length=100)
    annual_expenses = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=10)
    room_facilities = models.TextField(max_length=200)
    image1 = models.ImageField()
    image2 = models.ImageField()
    image3 = models.ImageField()


class BookRoom(models.Model):
    name = models.CharField(max_length=50)
    date_joining = models.DateField()
    booking_date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=0)


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


class Egrant(models.Model):
    name = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.CharField(max_length=50)
    academic_year = models.CharField(max_length=50)
    cast = models.CharField(max_length=50)
    yearly_income = models.CharField(max_length=100)
    approval_status = models.BooleanField(default=0)


class Fees(models.Model):
    name = models.ForeignKey(Student, on_delete=models.CASCADE)
    accommodation = models.IntegerField()
    water = models.IntegerField()
    electricity = models.IntegerField()
    caution_deposit = models.IntegerField()
    security = models.IntegerField()
    mess = models.IntegerField()
    others = models.IntegerField()
    e_grant = models.ForeignKey(Egrant, on_delete=models.CASCADE,)
    payment_status = models.BooleanField(default=False)

    def get_total_fee(self):
        if self.e_grant == True:
            return self.water + self.electricity + self.caution_deposit + self.security + self.mess + self.others

        else:
            return self.accommodation + self.water + self.electricity + self.caution_deposit + self.security + self.mess + self.others

    def __unicode__(self):
        return self.get_total_fee


class Payment(models.Model):
    student_name = models.ForeignKey(Student, on_delete=models.CASCADE)
    paid_by = models.CharField(max_length=100)
    date = models.DateField()
    payment = models.CharField(max_length=100)
    payment_status = models.BooleanField(default=False)

    def __str__(self):
        return self.paid_by


class Notification(models.Model):
    to = models.CharField(max_length=100)
    notification = models.TextField(max_length=100)
    time = models.TimeField()


class Attendance(models.Model):
    name = models.ForeignKey(Student, on_delete=models.CASCADE)
    initial_day = models.DateField()
    final_day = models.DateField()
    percentage = models.CharField(max_length=100)


class StaffRegister(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=10)
    email = models.EmailField()
    address = models.CharField(max_length=50)


class Review(models.Model):
    name = models.ForeignKey(Student, on_delete=models.CASCADE)
    review = models.TextField(max_length=200)
