from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django import forms

from adminmodule.models import User, AdminRegister, HostelDetails, Food, Income, Notification, StaffRegister


class AdminSignUpForm(UserCreationForm):
    name = forms.CharField(required=False)
    email = forms.CharField(required=False)
    phone_no = forms.CharField(max_length=10,required=False)
    address = forms.CharField(required=False)
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput,required=False)
    password2 = forms.CharField(label="confirm Password", widget=forms.PasswordInput,required=False)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_staff = False
        user.is_admin = True
        user.save()
        admin = AdminRegister.objects.create(user=user)
        admin.name = self.cleaned_data.get('name')
        admin.email = self.cleaned_data.get('email')
        admin.phone_no = self.cleaned_data.get('phone_no')
        admin.address = self.cleaned_data.get('address')
        admin.save()
        return user


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
        fields = ('name','mobile','email','address','username','password')


class UpdateStaffForm(forms.ModelForm):
    class Meta:
        model = StaffRegister
        fields = ('name','mobile','email','address','username','password')




