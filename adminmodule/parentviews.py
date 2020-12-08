from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from accounts.models import Parent
from adminmodule.models import Fees, Attendance, Food, Complaint, Notification, HostelDetails, StaffRegister


def parent_page(request):
    return render(request,'parent/parent_page.html')

def hostel_details(request):
    detail = HostelDetails.objects.all()
    return render(request,'parent/view_hostel_details.html',{'details':detail})

def staff_details(request):
    staff = StaffRegister.objects.all()
    return render(request,'parent/staff_detail.html',{'staffs':staff})
