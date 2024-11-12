from django.shortcuts import render
from .models import Task

# Create your views here.

def index(request):
    tasks = Task.objects.all().order_by("due_date")
    return render(request, "taskade/index.html", {'tasks': tasks})