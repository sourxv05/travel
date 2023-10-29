from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import place, staff


# Create your views here.
def demo(request):
    obj = place.objects.all()
    ob1 = staff.objects.all()

    return render(request, 'index.html', {'obj': obj,'ob1': ob1})

def log(request):
     if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
             auth.login(request,user)
             return redirect('/')
        else:
             messages.info(request,"invalid username ,password")
             return redirect('log')
     return render(request,'log.html')

def reg(request):
    if request.method=='POST':
        username=request.POST['username']
        firstname=request.POST['first_name']
        lastname=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"user name taken")
                return redirect("reg")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email taken")
                return redirect("reg")
            else:
                user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password)

                user.save()
                messages.info(request,"user created")
                return redirect('/log/')
        else:



            messages.info(request,'pasword doesnot match')
            return redirect('reg')
        return redirect('/')
    return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
