from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django import forms
from accounts.models import User, AdminRegister, Student,Parent


class AdminSignUpForm(UserCreationForm):
    name = forms.CharField()
    email = forms.CharField()
    phone_no = forms.CharField(max_length=10, )
    address = forms.CharField()
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput, )
    password2 = forms.CharField(label="confirm Password", widget=forms.PasswordInput, )

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_staff = True
        user.is_admin = True
        user.save()
        adm = AdminRegister.objects.create(user=user)
        adm.role = "Admin"
        adm.name = self.cleaned_data.get('name')
        adm.email = self.cleaned_data.get('email')
        adm.phone_no = self.cleaned_data.get('phone_no')
        adm.address = self.cleaned_data.get('address')
        adm.save()
        return user


class StudentSignUpForm(UserCreationForm):
    name = forms.CharField()
    email = forms.CharField()
    phone_no = forms.CharField(max_length=10, )
    address = forms.CharField()
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput,)
    password2 = forms.CharField(label="confirm Password", widget=forms.PasswordInput,)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_staff = False
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user)
        student.role = 'Student'
        student.name = self.cleaned_data.get('name')
        student.email = self.cleaned_data.get('email')
        student.phone_no = self.cleaned_data.get('phone_no')
        student.address = self.cleaned_data.get('address')
        student.save()
        return user


class ParentSignUpForm(UserCreationForm):
    student_name = forms.ModelChoiceField(queryset=Student.objects.all())
    name = forms.CharField()
    email = forms.CharField()
    phone_no = forms.CharField(max_length=10, required=False)
    address = forms.CharField()
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput,)
    password2 = forms.CharField(label="confirm Password", widget=forms.PasswordInput,)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_staff = False
        user.is_parent = True
        user.save()
        parent = Parent.objects.create(user=user)
        parent.role = 'Parent'
        parent.student_name = self.cleaned_data.get('student_name')
        parent.name = self.cleaned_data.get('name')
        parent.email = self.cleaned_data.get('email')
        parent.phone_no = self.cleaned_data.get('phone_no')
        parent.address = self.cleaned_data.get('address')
        parent.save()
        return user