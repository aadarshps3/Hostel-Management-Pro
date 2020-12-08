from django.contrib import auth, messages
from django.contrib.auth import login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse

from accounts.models import Student, Parent
from adminmodule.forms import AddHostelDetailsForm, UpdateHostelDetailsForm, AddFoodDetail, \
    AddIncomeDetailForm, AddStaffForm, UpdateStaffForm, UpdateFoodDetail, AddFeeForm, AddAttendanceForm
from adminmodule.models import HostelDetails, Food, Income, Complaint, Payment, Notification, Attendance, StaffRegister, \
    Fees


def admin_page(request):
    return render(request,'admin/admin_page.html')


def add_hostel_detail(request):
    form = AddHostelDetailsForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('view_hostel_detail')
    return render(request,'admin/add_hostel_details.html',{'form':form})


def view_hostel_detail(request):
    detail = HostelDetails.objects.all()
    return render(request,'admin/view_hostel_detail.html',{'details':detail})


def update_hostel_detail(request,id):
    detail = HostelDetails.objects.get(id=id)
    form = UpdateHostelDetailsForm(request.POST or None, instance=detail)
    if form.is_valid():
        form.save()
        return redirect('view_hostel_detail')
    return render(request,'admin/update_hostel_details.html',{'form':form})


def delete_hostel_detail(request, id):
    detail = HostelDetails.objects.get(id=id)
    if request.method == 'POST':
        detail.delete()
        return redirect('view_hostel_detail')
    return render(request,'admin/delete_hostel_detail.html')


def add_food_detail(request):
    form = AddFoodDetail(request.POST)
    if form.is_valid():
        form.save()
        return redirect('view_food_detail')
    return render(request,'admin/add_food_details.html',{'form':form})


def view_food_detail(request):
    food = Food.objects.all()
    return render(request,'admin/view_food_detail.html',{'foods':food})


def update_food_detail(request,id):
    detail = Food.objects.get(id=id)
    form = UpdateFoodDetail(request.POST or None, instance=detail)
    if form.is_valid():
        form.save()
        return redirect('view_food_detail')
    return render(request,'admin/update_food_details.html',{'form':form})


def delete_food_detail(request, id):
    detail = Food.objects.get(id=id)
    if request.method == 'POST':
        detail.delete()
        return redirect('view_food_detail')
    return render(request,'admin/delete_food_detail.html')


def add_income_detail(request):
    form = AddIncomeDetailForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('view_income_detail')
    return render(request,'admin/add_income_details.html',{'form':form})


def view_income_detail(request):
    income = Income.objects.all()
    return render(request,'admin/view_income_detail.html',{'incomes':income})


def view_complaint(request):
    complaint = Complaint.objects.all()
    return render(request,'admin/view_complaint.html',{'complaints':complaint})


def add_fee(request):
    form = AddFeeForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('view_fee')
    return render(request,'admin/add_fee.html',{'form':form})


def view_fee(request):
    fee = Fees.objects.all()
    return render(request,'admin/view_fee.html',{'fees':fee})


def view_payment(request):
    payment = Payment.objects.all()
    return render(request,'admin/view_payment.html',{'payments':payment})


def add_notification(request):
    if request.method == 'POST':
        to = request.POST.get('to')
        notification = request.POST.get('notification')
        time = request.POST.get('time')
        noti = Notification()
        noti.to = to
        noti.notification=notification
        noti.time=time
        noti.save()

        return redirect('view_notification')
    return render(request,'admin/add_notification.html',)


def view_notification(request):
    notification = Notification.objects.all()
    return render(request,'admin/view_notification.html',{'notifications':notification})


def add_attendance(request):
    form = AddAttendanceForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('view_attendance')
    return render(request,'admin/add_attendance.html',{'form':form})


def view_attendance(request):
    attendance = Attendance.objects.all()
    return render(request,'admin/view_attendance.html',{'attendances':attendance})


def add_staff(request):
    form = AddStaffForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('view_staff')
    return render(request,'admin/add_income_details.html',{'form':form})


def view_staff(request):
    staff = StaffRegister.objects.all()
    return render(request,'admin/view_staff.html',{'staffs':staff})


def update_staff(request,id):
    staff = StaffRegister.objects.get(id=id)

    form = UpdateStaffForm(request.POST or None, instance=staff)
    if form.is_valid():
        form.save()
        return redirect('view_staff')
    return render(request,'admin/update_staff.html',{'form':form})


def delete_staff(request, id):
    staff = StaffRegister.objects.get(id=id)
    if request.method == 'POST':
        staff.delete()
        return redirect('view_staff')
    return render(request,'admin/delete_staff.html')


def view_egrant_details(request):
    return render(request,'admin/view_egrant_details.html')


def view_registration_details(request):
    student = Student.objects.all()
    parent = Parent.objects.all()
    context = {
        'students':student,
        'parents':parent
    }
    return render(request,'admin/view_registration_details.html',context)


def approve_student(request,id):
    student = Student.objects.get(id=id)
    student.approval_status = True
    student.save()
    return HttpResponseRedirect(reverse('view_registration_details'))

def reject_student(request,id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        student.approval_status = False
        student.save()
        return redirect('view_registration_details')
    return render(request,'admin/reject_student.html')


def approve_parent(request,id):
    parent = Parent.objects.get(id=id)
    parent.approval_status = True
    parent.save()
    return HttpResponseRedirect(reverse('view_registration_details'))

def reject_parent(request,id):
    parent = Parent.objects.get(id=id)
    if request.method == 'POST':
        parent.approval_status = False
        parent.save()
        return redirect('view_registration_details')
    return render(request,'admin/reject_parent.html')