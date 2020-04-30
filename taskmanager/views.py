from django.shortcuts import render, get_object_or_404
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


# This view displays the tasks of a project
@login_required
def tasks_of_project(request, id_project):
    # Retrieves the corresponding project and its tasks
    project = get_object_or_404(Project, id=id_project)
    tasks = Task.objects.filter(project=project)

    return render(request, "taskmanager/tasks.html", {
        "project": project,
        "tasks": tasks
    })
