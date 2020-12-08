from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect

from accounts.models import Student
from adminmodule.forms import PayFeeForm, RegisterComplaintForm, AddReviewForm
from adminmodule.models import Fees, Attendance, Food, Complaint, Notification


def student_page(request):
    return render(request,'student/student_page.html')


def view_fee(request):
    # user = request.user
    # u = Student.objects.filter(id=user.id)
    # u = Student.objects.get(request.user)
    # print(u)
    fee = Fees.objects.filter(name=request.user)
    print(fee)
    return render(request,'student/view_fee.html',{'fees':fee})


def view_attendance(request):
    attendance = Attendance.objects.filter(name=request.user)
    return render(request,'student/view_attendance.html',{'attendances':attendance})


def pay_fee(request,):
    # fee = Fees.objects.get(id=id)
    form = PayFeeForm(request.POST)
    # if form.is_valid():

    return render(request,'student/pay_fee.html',{'form':form})


def view_food_updates(request):
    food = Food.objects.all()
    return render(request,'student/view_food_detail.html',{'foods':food})


def send_complaint(request):
    form = RegisterComplaintForm()
    if request.method == 'POST':
        form = RegisterComplaintForm(request.POST)
        if form.is_valid():
            comp = form.save(commit=False)
            comp.name = request.user
            comp.subject = form.cleaned_data.get('subject')
            comp.complaint = form.cleaned_data.get('complaint')
            comp.save()
            return redirect('view_send_compalints')

    else:
        form = RegisterComplaintForm()
    return render(request,'student/send_complaint.html',{'form':form})


def view_send_compalints(request):
    user = request.user
    complaint = Complaint.objects.filter(name=user)
    return render(request,'student/view_send_complaint.html',{'complaints':complaint})


def add_review(request):
    form = RegisterComplaintForm()
    if request.method == 'POST':
        form = AddReviewForm(request.POST)
        if form.is_valid():
            rev = form.save(commit=False)
            rev.name = request.user
            rev.review = form.cleaned_data.get('review')
            rev.save()

    else:
        form = AddReviewForm()
    return render(request,'student/add_review.html',{'form':form})


def view_notification(request):
    notification = Notification.objects.all()
    return render(request, "student/view_notification.html", {'notifications':notification})