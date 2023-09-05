from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from .models import User
# Create your views here.


def signup(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        User.objects.create_user(username=username,password=password)
        return redirect('/todo/')
    elif request.method=="GET":
        return render(request,"user/signup.html")


def signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user=authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('/todo/')
        else:
            return HttpResponse("Invalid auth",status=401)
    elif request.method=="GET":
        return render(request,"user/login.html")


def whoami(request):
    print(request.user)
    return HttpResponse(request.user)


def signout(request):
    if request.method=='POST':
        logout(request)
        return redirect("/todo/")
    else:
        return HttpResponse("Invalid auth", status=401)