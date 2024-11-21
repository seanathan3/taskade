from django import forms
from . import models

class CreateTask(forms.ModelForm):
    class Meta:
        model = models.Task
        fields = ['name', 'due_date', 'priority', 'thumb']
        