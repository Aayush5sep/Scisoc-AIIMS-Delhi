from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import UserDetails,Newsletter
from django.contrib.auth.decorators import login_required

# Create your views here.

def signuppage(request):
    return render(request,'user/signup.html')

def signupuser(request):
    if request.method=='POST':
        # Obtaining Data From The HTML Form
        username=request.POST['username']
        password=request.POST['password']
        cfpassword=request.POST['cfpassword']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        phone = request.POST['phone']
        age = request.POST['age']
        college = request.POST['college']
        events = request.POST.get('sub_event')
        fests = request.POST.get('sub_fest')

        if password != cfpassword:
            messages.error(request,"Passwords do not match")
            return redirect("/user/signuppage")

        # Default User Auth Save
        newuser = User.objects.create_user(username,email,password)
        newuser.first_name=fname
        newuser.last_name=lname
        newuser.save()
        user=authenticate(username=username,password=password)
        login(request,user)

        # Saving Extra Details About User
        userd=UserDetails(user=user,first_name=fname,last_name=lname,phone=phone,age=age,college=college)
        userd.save()

        # Subscribe For Fests/Events Newsletter
        sub_news = Newsletter(user=user)
        if events is not None:
            sub_news.event_sub = True
        if fests is not None:
            sub_news.fest_sub = True
        sub_news.save()

        messages.success(request,"User Account Created Successfully")
        return redirect("/")
    else:
        return HttpResponse("Creating new user account failed !")

def loginpage(request):
    return render(request,'user/login.html')

def loginuser(request):
    if request.method=='POST':
        login_username=request.POST['username']
        login_password=request.POST['password']

        user=authenticate(username=login_username,password=login_password)
        if user is not None:
            login(request,user)
            messages.success(request,'Login Successful')
            return redirect("/")
        else:
            messages.error(request,'Login Failed')
            return HttpResponse("Oops! Login Failed")
    else:
        return HttpResponse("Unsecured Login Error !!")

@login_required(login_url='user/login/')
def logoutuser(request):
    logout(request)
    messages.success(request,'Logout Successful')
    return redirect("/")


@login_required(login_url='user/login/')
def profile(request):
    return render(request,'user/profile.html')

@login_required(login_url='user/login/')
def profileupd(request):
    if request.method=='POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        phone = request.POST['phone']
        age = request.POST['age']
        college = request.POST['college']
        UserDetails(first_name=fname,last_name=lname,phone=phone,age=age,college=college).save()
        messages.success(request,'Profile Updated')
    else:
        messages.error(request,'Invalid Request')
    return redirect("/")