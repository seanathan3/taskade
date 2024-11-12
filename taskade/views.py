from django.shortcuts import render
from .models import Task
from django.http import HttpResponse

# Create your views here.

def index(request):
    tasks = Task.objects.all().order_by("due_date")
    return render(request, "taskade/index.html", {'tasks': tasks})

def detail(request, id):
    task = Task.objects.filter(id=id)
    return HttpResponse(id)