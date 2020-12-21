from django.contrib import messages
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.shortcuts import render, redirect
from accounts.models import Parent, Student
from adminmodule.forms import StudentBookRoomForm, StudentPaymentForm
from adminmodule.models import Fees, Attendance, Food, Complaint, Notification, HostelDetails, StaffRegister, BookRoom, \
    Egrant, Payment


def parent_page(request):
    return render(request,'parent/parent_page.html')

def hostel_details(request):
    detail = HostelDetails.objects.all()
    return render(request,'parent/view_hostel_details.html',{'details':detail})


def staff_details(request):
    staff = StaffRegister.objects.all()
    return render(request,'parent/staff_detail.html',{'staffs':staff})


def book_room_parent(request):
    form = StudentBookRoomForm()
    if request.method == 'POST':
        form = StudentBookRoomForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.name = request.user
            book.date_joining = form.cleaned_data.get('date_joining')
            book.booking_date = form.cleaned_data.get('booking_date')
            book.save()
            return redirect('booking_status_parent')
    return render(request,'parent/book_room.html',{'form':form})


def booking_status_parent(request):
    status = BookRoom.objects.filter(name=request.user)
    return render(request,'parent/booking_status.html',{'statuss':status})


def cancel_booking_parent(request,id):
    book = BookRoom.objects.filter(pk=id)
    if request.method == 'POST':
        book.delete()
        messages.info(request,'Your Booking Has Been Cancelled')
        return redirect('booking_status_parent')
    return render(request,'parent/cancel_booking.html')


def student_attendance(request):
    u = Parent.objects.get(user=request.user)
    attendance = Attendance.objects.filter(name=u.student_name)
    return render(request,'parent/student_attendance.html',{'attendances':attendance})


def student_egrant(request):
    u = Parent.objects.get(user=request.user)
    egrant = Egrant.objects.filter(name=u.student_name)
    return render(request,'parent/egrant_status.html',{'egrants':egrant})

def parent_fee_view(request):
    u = Parent.objects.get(user=request.user)
    fee = Fees.objects.filter(name=u.student_name)
    return render(request,'parent/fees_view_parent.html',{'fees':fee})

def parent_pay_fee(request,id):
    parent = Parent.objects.get(user=request.user)
    fee = Fees.objects.get(id=id)
    total = fee.get_total_fee
    try:
        if fee.e_grant.approval_status == True:
            total = fee.water + fee.electricity + fee.caution_deposit + fee.security + fee.mess + fee.others
    except ObjectDoesNotExist:
        total = fee.accommodation + fee.water + fee.electricity + fee.caution_deposit + fee.security + fee.mess + fee.others

    if request.method == 'POST':

        payment = request.POST.get('payment')
        date = request.POST.get('date')
        ob = Payment()
        ob.student_name = parent.student_name
        ob.paid_by = parent.name
        ob.payment = payment
        ob.date = date
        ob.payment_status = True
        ob.save()
        fee.payment_status = True
        fee.save()
        return redirect('payment_details_parent')
    return render(request,'parent/parent_pay_fee.html',{'total': total})


def payment_details_parent(request):
    u = Parent.objects.get(user=request.user)
    payment = Payment.objects.filter(student_name=u.student_name)
    return render(request,'parent/payment_details.html',{'payments':payment})
