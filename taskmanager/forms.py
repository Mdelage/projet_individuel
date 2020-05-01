from django import forms
from .models import Task


# This form represents the form to add a task to a project
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ['project']
