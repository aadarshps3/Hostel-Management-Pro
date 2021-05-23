from django.contrib import auth, messages
from django.contrib.auth import login, logout
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from accounts.models import Student, Parent
from adminmodule.forms import AddHostelDetailsForm, UpdateHostelDetailsForm, AddFoodDetail, \
    AddIncomeDetailForm, AddStaffForm, UpdateStaffForm, UpdateFoodDetail, AddFeeForm, AddAttendanceForm, \
    NotificationForm
from adminmodule.models import HostelDetails, Food, Income, Complaint, Payment, Notification, Attendance, StaffRegister, \
    Fees, BookRoom, Egrant, Review


def admin_page(request):
    return render(request, 'adminpages/home.html')


def add_hostel_detail(request):
    form = AddHostelDetailsForm()
    if request.method == 'POST':
        form = AddHostelDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            hostel = form.save(commit=False)
            hostel.total_rooms = form.cleaned_data.get('total_rooms')
            hostel.occupied = form.cleaned_data.get('occupied')
            hostel.annual_expenses = form.cleaned_data.get('annual_expenses')
            hostel.location = form.cleaned_data.get('location')
            hostel.contact_no = form.cleaned_data.get('contact_no')
            hostel.room_facilities = form.cleaned_data.get('room_facilities')
            hostel.image1 = request.FILES['image1']
            hostel.image2 = request.FILES['image2']
            hostel.image3 = request.FILES['image3']
            fs = FileSystemStorage()
            hostel.save()
            messages.info(request,'Hostel Details Added')
            return redirect('view_hostel_detail')
    return render(request, 'adminpages/add_hostel_details.html', {'form': form})


def view_hostel_detail(request):
    detail = HostelDetails.objects.all()
    return render(request, 'adminpages/view_hostel_detail.html', {'details': detail})


def update_hostel_detail(request, id):
    detail = HostelDetails.objects.get(id=id)
    form = UpdateHostelDetailsForm(request.POST or None, instance=detail)
    if form.is_valid():
        form.save()
        messages.info(request, 'Hostel Details Updated Successfully')
        return redirect('view_hostel_detail')
    return render(request, 'adminpages/update_hostel_details.html', {'form': form})


def delete_hostel_detail(request, id):
    detail = HostelDetails.objects.get(id=id)
    if request.method == 'POST':
        detail.delete()
        messages.info(request, 'Hostel Details Deleted Successfully')
        return redirect('view_hostel_detail')
    return render(request, 'adminpages/delete_hostel_detail.html')


def add_food_detail(request):
    form = AddFoodDetail()
    if request.method == 'POST':
        form = AddFoodDetail(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Food Details Added Successfully')
            return redirect('view_food_detail')
    return render(request, 'adminpages/add_food_details.html', {'form': form})


def view_food_detail(request):
    food = Food.objects.all()
    return render(request, 'adminpages/view_food_detail.html', {'foods': food})


def update_food_detail(request, id):
    detail = Food.objects.get(id=id)
    form = UpdateFoodDetail(request.POST or None, instance=detail)
    if form.is_valid():
        form.save()
        messages.info(request, 'Food Details Updated Successfully')
        return redirect('view_food_detail')
    return render(request, 'adminpages/update_food_details.html', {'form': form})


def delete_food_detail(request, id):
    detail = Food.objects.get(id=id)
    if request.method == 'POST':
        detail.delete()
        messages.info(request, 'Food Details Deleted Successfully')
        return redirect('view_food_detail')
    return render(request, 'adminpages/delete_food_detail.html')


def add_income_detail(request):
    form = AddIncomeDetailForm()
    if request.method == 'POST':
        form = AddIncomeDetailForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Income Details Updated Successfully')
            return redirect('view_income_detail')
    return render(request, 'adminpages/add_income_details.html', {'form': form})


def view_income_detail(request):
    income = Income.objects.all()
    return render(request, 'adminpages/view_income_detail.html', {'incomes': income})


def view_complaint(request):
    complaint = Complaint.objects.all()
    return render(request, 'adminpages/view_complaint.html', {'complaints': complaint})


def add_fee(request):
    form = AddFeeForm()
    if request.method == 'POST':
        form = AddFeeForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            name = form.cleaned_data.get('name')
            accommadation = form.cleaned_data.get('accommadation')
            water = form.cleaned_data.get('water')
            electricity = form.cleaned_data.get('electricity')
            caution_deposit = form.cleaned_data.get('caution_deposit')
            security = form.cleaned_data.get('security')
            mess = form.cleaned_data.get('mess')
            others = form.cleaned_data.get('others')
            form.save()
            messages.info(request, 'Fee Added Successfully')
            return redirect('view_fee')

    return render(request, 'adminpages/add_fee.html', {'form': form})


def view_fee(request):
    fee = Fees.objects.all()
    return render(request, 'adminpages/view_fee.html', {'fees': fee})


def view_payment(request):
    payment = Payment.objects.all()
    return render(request, 'adminpages/view_payment.html', {'payments': payment})


def add_notification(request):
    form = NotificationForm()
    if request.method == 'POST':
        form = NotificationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Notification Added Successfully')
            return redirect('view_notification')
    return render(request, 'adminpages/add_notification.html', {'form': form})


def view_notification(request):
    notification = Notification.objects.all()
    return render(request, 'adminpages/view_notification.html', {'notifications': notification})


def add_attendance(request):
    form = AddAttendanceForm()
    if request.method == 'POST':
        form = AddAttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Attendance Added Successfully')
            return redirect('view_attendance')
    return render(request, 'adminpages/add_attendance.html', {'form': form})


def view_attendance(request):
    attendance = Attendance.objects.all()
    return render(request, 'adminpages/view_attendance.html', {'attendances': attendance})


def add_staff(request):
    form = AddStaffForm()
    if request.method == 'POST':
        form = AddStaffForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Staff Added Successfully')
            return redirect('view_staff')

    return render(request, 'adminpages/add_staff.html', {'form': form})


def view_staff(request):
    staff = StaffRegister.objects.all()
    return render(request, 'adminpages/view_staff.html', {'staffs': staff})


def update_staff(request, id):
    staff = StaffRegister.objects.get(id=id)

    form = UpdateStaffForm(request.POST or None, instance=staff)
    if form.is_valid():
        form.save()
        messages.info(request, 'Staff Updated Successfully')
        return redirect('view_staff')
    return render(request, 'adminpages/update_staff.html', {'form': form})


def delete_staff(request, id):
    staff = StaffRegister.objects.get(id=id)
    if request.method == 'POST':
        staff.delete()
        messages.info(request, 'Staff Deleted Successfully')
        return redirect('view_staff')
    return render(request, 'adminpages/delete_staff.html')


def view_registration_details(request):
    student = Student.objects.all()
    parent = Parent.objects.all()
    context = {
        'students': student,
        'parents': parent
    }
    return render(request, 'adminpages/view_registration_details.html', context)


def approve_student(request, id):
    student = Student.objects.get(user_id=id)
    student.approval_status = True
    student.save()
    messages.info(request, 'Student Approved  Successfully')
    return HttpResponseRedirect(reverse('view_registration_details'))


def reject_student(request, id):
    student = Student.objects.get(user_id=id)
    if request.method == 'POST':
        student.approval_status = False
        student.save()
        messages.info(request, 'Rejected Student Registration')
        return redirect('view_registration_details')
    return render(request, 'adminpages/reject_student.html')


def approve_parent(request, id):
    parent = Parent.objects.get(user_id=id)
    parent.approval_status = True
    parent.save()
    messages.info(request, 'Parent Approved  Successfully')
    return HttpResponseRedirect(reverse('view_registration_details'))


def reject_parent(request, id):
    parent = Parent.objects.get(user_id=id)
    if request.method == 'POST':
        parent.approval_status = False
        parent.save()
        messages.info(request, 'Rejected Parent Registration')
        return redirect('view_registration_details')
    return render(request, 'adminpages/reject_parent.html')


def bookings(request):
    book = BookRoom.objects.all()
    return render(request, 'adminpages/bookings.html', {'books': book})


def confirm_booking(request, id):
    book = BookRoom.objects.get(id=id)
    book.status = True
    book.save()

    hstl = HostelDetails.objects.all().last()
    occupied = hstl.occupied
    hstl.occupied = int(occupied)-1
    hstl.save()
    messages.info(request, 'Room Booking Confirmed')
    return HttpResponseRedirect(reverse('bookings'))


def reject_booking(request, id):
    book = BookRoom.objects.get(id=id)
    if request.method == 'POST':
        book.status = False
        book.save()
        messages.info(request, 'Room Booking rejected')
        return redirect('bookings')
    return render(request, 'adminpages/reject_booking.html')


def view_egrant_details(request):
    egrant = Egrant.objects.all()
    return render(request, 'adminpages/view_egrant_applications.html', {'egrants': egrant})


def approve_egrant(request, id):
    egrant = Egrant.objects.get(id=id)
    egrant.approval_status = True
    egrant.save()
    messages.info(request, 'E grant Approved')
    return HttpResponseRedirect(reverse('view_egrant_details'))


def reject_egrant(request, id):
    egrant = Egrant.objects.get(id=id)
    if request.method == 'POST':
        egrant.status = False
        egrant.save()
        messages.info(request, 'E grant Rejected')
        return redirect('view_egrant_details')
    return render(request, 'adminpages/reject_booking.html')


def review(request):
    review = Review.objects.all()
    return render(request, 'adminpages/reviews.html', {'reviews': review})
