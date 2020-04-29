from django.shortcuts import render, redirect
from taskmanager import views


# This view redirects the user to the login page, in the taskmanager app
def welcome(request):
    return redirect('taskmanager/login/', permanent=True)
