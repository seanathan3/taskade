import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=200)
    created_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    priority = models.IntegerField()
    thumb = models.ImageField(default="default.png", blank=True)
    creator = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def overdue(self):
        return self.due_date < datetime.date.today()
