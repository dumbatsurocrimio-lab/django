from django.shortcuts import HttpResponse
from django.shortcuts import render


def hello_world_view(request):
    return HttpResponse("Hello, world!")

def hello_Joseph_view(request):
    return HttpResponse("Hello, Joseph!")

def html_view(request):
    return render(request, 'todos/index.html') k