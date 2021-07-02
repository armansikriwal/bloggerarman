from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login ,logout


# Create your views here.
def register(request):
    if request.method =="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"user name taken")
                return redirect("register")
            elif User.objects.filter(email=email).exists(): 
                messages.info(request," email already exists")
                return redirect("register")

            else:
                user= User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                return redirect("login")
        else :
            messages.info(request,"password doesnt match")
            return redirect("register")
        return redirect("/")
    else:
        return render(request,"register.html")


def login_req(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            messages.info(request,"enter valid details")
            return redirect("login")
    else:
        return render(request,"login.html")

def logout_view(request):
    logout(request)
    return redirect("/")