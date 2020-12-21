from django.contrib import auth, messages
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from accounts.forms import AdminSignUpForm, StudentSignUpForm, ParentSignUpForm
from adminmodule import views,studentviews,parentviews



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            if user.is_admin:
                return redirect('admin_page')
            elif user.is_student:
                return redirect('student_page')
            else:
                return redirect('parent_page')

        else:
            messages.info(request,"Inavlid Credentials")
    return render(request,'login.html')


def logout_view(request):
    logout(request)
    return redirect('/')


def select_role(request):
    if request.method == 'POST':
        role = request.POST.get('role')
        if role == 'Admin':
            return redirect('accounts:admin_register')
        elif role == 'Student':
            return redirect('accounts:student_register')
        elif role == 'Parent':
            return redirect('accounts:parent_register')
        else:
            messages.info(request,'Please Choose Your Type')

    return render(request,'select_role.html')


def admin_register(request):
    form = AdminSignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        return redirect('accounts:login_view')
    return render(request,'admin/admin_register.html', {'form':form})


def student_register(request):
    form = StudentSignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        return redirect('accounts:login_view')
    return render(request,'student/student_register.html', {'form':form})


def parent_register(request):
    form = ParentSignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        return redirect('accounts:login_view')
    return render(request,'parent/parent_register.html', {'form':form})

