from django.shortcuts import render
from .models import Task
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    tasks = Task.objects.all().order_by("due_date")
    return render(request, "taskade/index.html", {'tasks': tasks})

def detail(request, id):
    task = Task.objects.get(id=id)
    return render(request, "taskade/detail.html", {'task': task})

@login_required(login_url="/accounts/login/")
def create(request):
    return render(request, "taskade/create.html")