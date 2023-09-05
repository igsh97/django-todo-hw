from django.http import HttpResponse
from django.shortcuts import render

def pingpong(request):
    print(request)
    return render(request,'pong.html')


def index(request):
    name=request.GET.get('name')
    return render(request,'index.html')


def receive(request):
    print(request.POST.get('todo'))
    print(request.POST.get('todo2'))
    print(request.POST.get('todo3'))
    return HttpResponse('ok')
