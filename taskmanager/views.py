from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *


# This view displays all the projects
@login_required
def projects(request):
    # This dictionnary contains the lists of all users per project
    users_per_project = {}
    for project in Project.objects.all():
        users_per_project[project] = project.users.all()

    return render(request, "taskmanager/projects.html", {'users_per_project': users_per_project})
