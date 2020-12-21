from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django import forms
from django.forms import Textarea

from accounts.models import Student,Parent
from adminmodule.models import HostelDetails, Food, Income, Notification, StaffRegister, Fees, Attendance, Payment, \
    Complaint, Review, BookRoom, Egrant

class DateInput(forms.DateInput):
    input_type = 'date'


class AddHostelDetailsForm(forms.ModelForm):
    class Meta:
        model = HostelDetails
        fields = ('total_rooms','occupied','annual_expenses','location','contact_no','room_facilities','image1','image2','image3')
        widgets = {
            'image1':forms.FileInput(attrs={'class':'form-control'}),
            'image2':forms.FileInput(attrs={'class':'form-control'}),
            'image3':forms.FileInput(attrs={'class':'form-control'}),
        }


class UpdateHostelDetailsForm(forms.ModelForm):
    class Meta:
        model = HostelDetails
        fields = ('total_rooms','occupied','annual_expenses','location','contact_no','room_facilities','image1','image2','image3')


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
    initial_day = forms.DateField(required=True, widget=forms.DateInput(attrs={'placeholder': 'MM/DD/YYYY'}))
    final_day = forms.DateField(required=True, widget=forms.DateInput(attrs={'placeholder': 'MM/DD/YYYY'}))
    class Meta:
        model = Attendance
        fields = ('name','initial_day','final_day','percentage')


class StudentPaymentForm(forms.ModelForm):
    payment = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    date = forms.DateField(required=True,widget=DateInput())
    class Meta:
        model = Payment
        fields = ('payment','date')


class RegisterComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ('subject','complaint')


class AddReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('review',)

class StudentBookRoomForm(forms.ModelForm):
    date_joining = forms.DateField(required=True,widget=forms.DateInput(attrs={'placeholder':'MM/DD/YYYY'}))
    class Meta:
        model = BookRoom
        fields = ('date_joining',)


class ApplyEgrantForm(forms.ModelForm):
    class Meta:
        model = Egrant
        fields = ('course','academic_year','cast','yearly_income')


