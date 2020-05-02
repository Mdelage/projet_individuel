from django.shortcuts import render, redirect


# This view redirects the user to the projects page, in the taskmanager app
def welcome(request):
    return redirect('view_all_projects', permanent=True)
