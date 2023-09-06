from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from .models import User
from todo.models import Todo
# Create your views here.


def signup(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        email = request.POST["email"]
        profile=request.POST["profile"]
        profile_image = request.FILES.get("profile_image")
        User.objects.create_user(
            username=username,
            password=password,
            email=email,
            profile=profile,
            profile_image=profile_image,
        )
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


def mypage(request,id):
    my_todos=Todo.objects.filter(user_id=id)
    user=User.objects.get(id=id)
    context={'my_todos':my_todos,'user':user}
    return render(request,'user/mypage.html',context=context)