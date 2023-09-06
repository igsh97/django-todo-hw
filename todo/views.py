from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from todo.models import Todo
# Create your views here.


def index(request):
    if request.method=='GET':
        todos=Todo.objects.all()
        context={
            "todos":todos
        }
        return render(request,"todo/index.html",context=context)
    else:
        return HttpResponse("Invalid request method",status=405)


@login_required(login_url='/user/signin')
def create(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            Todo.objects.create(
                content=request.POST["content"],
                user=request.user,
                image=request.FILES.get("image"),
            )
            return redirect('/todo/')
        elif request.method=="GET":
            return render(request,"todo/create.html")
    else :
        return redirect("/user/signin/")


def read(request,todo_id):
    todo=Todo.objects.get(id=todo_id)
    context = {
        "todo": todo
    }
    return render(request, "todo/detail.html", context=context)


def delete(request,todo_id):
    if request.method=='POST':
        todo=Todo.objects.get(id=todo_id)
        if request.user == todo.user:
            todo.delete()
            return redirect('/todo/')
        else:
            return HttpResponse("You are not allowed to delete this todo", status=403)
    else:
        return HttpResponse("Invalid request method",status=405)


def update(request, todo_id):
    if request.method == "POST":
        todo = Todo.objects.get(id=todo_id)
        if request.user != todo.user:
            return HttpResponse("You are not allowed to delete this todo", status=403)
        todo.content = request.POST["content"]
        todo.save()
        return redirect(f'/todo/')
    elif request.method == "GET":
        todo=Todo.objects.get(id=todo_id)
        context={
            "todo":todo,
        }
        return render(request,"todo/update.html",context=context)