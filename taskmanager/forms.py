from django import forms
from .models import Task, History


# This form represents the form to add a task to a project
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ['project']


# This form represents the form to add en entry to a task
class HistoryForm(forms.ModelForm):
    class Meta:
        model = History
        exclude = ['task', 'author', 'date']
