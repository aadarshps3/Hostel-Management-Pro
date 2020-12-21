from django.contrib import messages
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.shortcuts import render, redirect
from accounts.models import Student
from adminmodule.forms import StudentPaymentForm, RegisterComplaintForm, AddReviewForm, StudentBookRoomForm, ApplyEgrantForm
from adminmodule.models import Fees, Attendance, Food, Complaint, Notification, HostelDetails, BookRoom, Egrant, Payment


def student_page(request):
    return render(request,'student/student_page.html')


def view_hostel_details(request):
    detail = HostelDetails.objects.all()
    return render(request,'student/view_hostel_details.html',{'details':detail})

def book_room(request):
    form = StudentBookRoomForm()
    if request.method == 'POST':
        form = StudentBookRoomForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.name = request.user
            book.date_joining = form.cleaned_data.get('date_joining')
            book.booking_date = form.cleaned_data.get('booking_date')
            book.save()
            return redirect('booking_status')
    return render(request,'student/book_room.html',{'form':form})

def booking_status(request):
    status = BookRoom.objects.filter(name=request.user)
    return render(request,'student/booking_status.html',{'statuss':status})

def cancel_booking(request,id):
    book = BookRoom.objects.filter(pk=id)
    if request.method == 'POST':
        book.delete()
        messages.info(request,'Your Booking Has Been Cancelled')
        return redirect('booking_status')
    return render(request,'student/cancel_booking.html')


def view_attendance(request):
    u = Student.objects.get(user=request.user)
    attendance = Attendance.objects.filter(name=u)
    return render(request,'student/view_attendance.html',{'attendances':attendance})


def apply_egrant(request):
    form = ApplyEgrantForm()
    if request.method == 'POST':
        form = ApplyEgrantForm(request.POST)
        if form.is_valid():
            egrant = form.save(commit=False)
            egrant.name = Student.objects.get(user=request.user)
            egrant.course = form.cleaned_data.get('course')
            egrant.academic_year = form.cleaned_data.get('academic_year')
            egrant.cast = form.cleaned_data.get('cast')
            egrant.yearly_income = form.cleaned_data.get('yearly_income')
            egrant.save()
            return redirect('egrant_status')
    return render(request,'student/apply_egrant.html',{'form':form})


def egrant_status(request):
    u = Student.objects.get(user=request.user)
    egrant = Egrant.objects.filter(name=u)
    return render(request,'student/egrant_status.html',{'egrants':egrant})


def view_fee(request):
    u = Student.objects.get(user=request.user)
    fee = Fees.objects.filter(name=u)
    return render(request,'student/fees_view_student.html',{'fees':fee})



def pay_fee(request,id):
    u = Student.objects.get(user=request.user)
    fee = Fees.objects.get(id=id)
    total = fee.get_total_fee
    try:
        if fee.e_grant.approval_status==True:
            total=fee.water + fee.electricity + fee.caution_deposit + fee.security + fee.mess + fee.others
    except ObjectDoesNotExist:
        total=fee.accommodation + fee.water + fee.electricity + fee.caution_deposit + fee.security + fee.mess + fee.others

    if request.method == 'POST':
        payment = request.POST.get('payment')
        date = request.POST.get('date')
        ob = Payment()

        ob.student_name = u
        ob.paid_by = u.name
        ob.payment = payment
        ob.date = date
        ob.payment_status = True
        ob.save()
        fee.payment_status = True
        fee.save()
        return redirect('payment_details')
    return render(request, 'student/pay_fee.html', {'total': total})


def payment_details(request):
    u = Student.objects.get(user=request.user)
    payment = Payment.objects.filter(student_name=u)
    return render(request,'student/payment_details.html',{'payments':payment})

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
            rev.name = Student.objects.get(user=request.user)
            rev.review = form.cleaned_data.get('review')
            rev.save()


    else:
        form = AddReviewForm()
    return render(request,'student/add_review.html',{'form':form})


def view_notification(request):
    notification = Notification.objects.all()
    return render(request, "student/view_notification.html", {'notifications':notification})