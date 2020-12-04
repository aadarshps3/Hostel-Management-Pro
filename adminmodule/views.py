from django.contrib import auth, messages
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect


# Create your views here.
from adminmodule.forms import AdminSignUpForm, AddHostelDetailsForm, UpdateHostelDetailsForm, AddFoodDetail, \
    AddIncomeDetailForm, AddStaffForm, UpdateStaffForm, UpdateFoodDetail
from adminmodule.models import HostelDetails, Food, Income, Complaint, Payment, Notification, Attendance, StaffRegister


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            if user.is_admin:
                return redirect('admin_page')

        else:
            messages.info(request,"Inavlid Credentials")

    return render(request,'login.html')

def logout_view(request):
    logout(request)
    return redirect('/')


def admin_register(request):
    form = AdminSignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        return redirect('login_view')
    return render(request,'admin_register.html', {'form':form})

# hhhhhhhhhhhhhhhhhhhhhh
def admin_page(request):
    return render(request,'admin_page.html')


def add_hostel_detail(request):
    form = AddHostelDetailsForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('view_hostel_detail')
    return render(request,'add_hostel_details.html',{'form':form})


def view_hostel_detail(request):
    detail = HostelDetails.objects.all()
    return render(request,'view_hostel_detail.html',{'details':detail})


def update_hostel_detail(request,id):
    detail = HostelDetails.objects.get(id=id)
    form = UpdateHostelDetailsForm(request.POST or None, instance=detail)
    if form.is_valid():
        form.save()
        return redirect('view_hostel_detail')
    return render(request,'update_hostel_details.html',{'form':form})


def delete_hostel_detail(request, id):
    detail = HostelDetails.objects.get(id=id)
    if request.method == 'POST':
        detail.delete()
        return redirect('view_hostel_detail')
    return render(request,'delete_hostel_detail.html')


def add_food_detail(request):
    form = AddFoodDetail(request.POST)
    if form.is_valid():
        form.save()
        return redirect('view_food_detail')
    return render(request,'add_food_details.html',{'form':form})


def view_food_detail(request):
    food = Food.objects.all()
    print(food)
    return render(request,'view_food_detail.html',{'foods':food})



def update_food_detail(request,id):
    detail = Food.objects.get(id=id)
    form = UpdateFoodDetail(request.POST or None, instance=detail)
    if form.is_valid():
        form.save()
        return redirect('view_food_detail')
    return render(request,'update_food_details.html',{'form':form})


def delete_food_detail(request, id):
    detail = Food.objects.get(id=id)
    if request.method == 'POST':
        detail.delete()
        return redirect('view_food_detail')
    return render(request,'delete_food_detail.html')


def add_income_detail(request):
    form = AddIncomeDetailForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('view_income_detail')
    return render(request,'add_income_details.html',{'form':form})

def view_income_detail(request):
    income = Income.objects.all()
    return render(request,'view_income_detail.html',{'incomes':income})


def view_complaint(request):
    complaint = Complaint.objects.all()
    return render(request,'view_complaint.html',{'complaints':complaint})


def view_payment(request):
    payment = Payment.objects.all()
    return render(request,'view_payment.html',{'payments':payment})


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
    return render(request,'add_notification.html',)



def view_notification(request):
    notification = Notification.objects.all()
    return render(request,'view_notification.html',{'notifications':notification})


def view_attendance(request):
    attendance = Attendance.objects.all()
    return render(request,'view_attendance.html',{'attendances':attendance})


def add_staff(request):
    form = AddStaffForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('view_staff')
    return render(request,'add_income_details.html',{'form':form})

def view_staff(request):
    staff = StaffRegister.objects.all()
    return render(request,'view_staff.html',{'staffs':staff})


def update_staff(request,id):
    staff = StaffRegister.objects.get(id=id)
    form = UpdateStaffForm(request.POST or None, instance=staff)
    if form.is_valid():
        form.save()
        return redirect('view_staff')
    return render(request,'update_staff.html',{'form':form})


def delete_staff(request, id):
    staff = StaffRegister.objects.get(id=id)
    if request.method == 'POST':
        staff.delete()
        return redirect('view_staff')
    return render(request,'delete_staff.html')

def view_egrant_details(request):
    return render(request,'view_egrant_details.html')


def view_registration_details(request):
    return render(request,'view_registration_details.html')

def index(request):
    return render(request,'index.html')