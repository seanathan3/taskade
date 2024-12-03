from django.shortcuts import render, redirect
from .models import Task
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
# Create your views here.

def index(request):
    tasks = Task.objects.all().order_by("due_date")
    return render(request, "taskade/index.html", {'tasks': tasks})

def detail(request, id):
    task = Task.objects.get(id=id)
    return render(request, "taskade/detail.html", {'task': task})

@login_required(login_url="/accounts/login/")
def create(request):
    if request.method == 'POST':
        form = forms.CreateTask(request.POST, request.FILES)
        if form.is_valid():
            # save to DB
            instance = form.save(commit=False)
            instance.creator = request.user
            instance.save()
            return redirect("tasks:index")
    else:
        form = forms.CreateTask()
    return render(request, "taskade/create.html", {"form": form})

def complete(request, id):
    if request.method == 'POST':
        task = Task.objects.get(id=id)
        task.completed = True
        task.save()
        return redirect('tasks:index')