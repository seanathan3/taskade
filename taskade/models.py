import datetime
from django.db import models

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=200)
    created_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    priority = models.IntegerField()
    # add in owner later

    def __str__(self):
        return self.name
    
    def overdue(self):
        return self.due_date < datetime.date.today()
