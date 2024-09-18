import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=200)
    created_time = models.DateTimeField()
    due_date = models.DateField()
    priority = models.IntegerField()

    def __str__(self):
        return self.name
    
    def was_published_recently(self):
        return self.created_time >= timezone.now() - datetime.timedelta(days=1)
