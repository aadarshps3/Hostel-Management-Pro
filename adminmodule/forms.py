from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django import forms
from django.forms import Textarea

from accounts.models import Student,Parent
from adminmodule.models import HostelDetails, Food, Income, Notification, StaffRegister, Fees, Attendance, Payment, \
    Complaint, Review


class AddHostelDetailsForm(forms.ModelForm):
    class Meta:
        model = HostelDetails
        fields = ('total_rooms','occupied','annual_expenses','location','contact_no')



class UpdateHostelDetailsForm(forms.ModelForm):
    class Meta:
        model = HostelDetails
        fields = ('total_rooms','occupied','annual_expenses','location','contact_no')


class AddFoodDetail(forms.ModelForm):
    class Meta:
        model = Food
        fields = ('breakfast','lunch','dinner')

class UpdateFoodDetail(forms.ModelForm):
    class Meta:
        model = Food
        fields = ('breakfast','lunch','dinner')



class AddIncomeDetailForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ('received','given','total_income')

class AddStaffForm(forms.ModelForm):
    class Meta:
        model = StaffRegister
        fields = ('name','mobile','email','address',)


class UpdateStaffForm(forms.ModelForm):
    class Meta:
        model = StaffRegister
        fields = ('name','mobile','email','address',)


class AddFeeForm(forms.ModelForm):
    name = forms.ModelChoiceField(queryset=Student.objects.all())
    class Meta:
        model = Fees
        fields = ('name','accommodation','water','electricity','caution_deposit','security','mess','others')


class AddAttendanceForm(forms.ModelForm):
    name = forms.ModelChoiceField(queryset=Student.objects.all())
    class Meta:
        model = Attendance
        fields = ('name','initial_day','final_day','percentage')


class PayFeeForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ('payment','e_grant')


class RegisterComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ('subject','complaint')

class AddReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('review',)

