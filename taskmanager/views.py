from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *


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


# This view displays the details of a task
@login_required
def details_of_task(request, id_project, id_task):
    # Retrieves the corresponding project, task and its entries
    project = get_object_or_404(Project, id=id_project)
    task = get_object_or_404(Task, project=project, id=id_task)
    entries = History.objects.filter(task=task)

    return render(request, "taskmanager/details.html", locals())


# This view allows the user to add a task to project
@login_required
def add_a_task(request, id_project):
    # Retrieves the corresponding project
    project = get_object_or_404(Project, id=id_project)
    # Retrieves the user participating in the project
    users = project.users.all()
    # Create a task from this project, with the other fields empty
    task = Task(project=project)
    # Create the associated form
    form = TaskForm(
        request.POST or None,
        instance=task,
    )

    envoi = False

    if form.is_valid():
        task.name = form.cleaned_data['name']
        task.description = form.cleaned_data['description']

        # The assignee field is not a part of the form.
        # We retrieve it via the POST parameter (see create-task.html).
        assignee = User.objects.get(id=request.POST['assignee'])
        task.assignee = assignee

        task.start_date = form.cleaned_data['start_date']
        task.due_date = form.cleaned_data['due_date']
        task.priority = form.cleaned_data['priority']
        task.status = form.cleaned_data['status']

        task.save()

        envoi = True

    return render(request, 'taskmanager/create-task.html', locals())


# This view allows the user to modify an existing task
@login_required
def modify_a_task(request, id_project, id_task):
    # Retrieves the corresponding project and task
    project = get_object_or_404(Project, id=id_project)
    task = get_object_or_404(Task, id=id_task)
    # Retrieves the user participating in the project
    users = project.users.all()
    # Create the associated form
    form = TaskForm(request.POST or None, instance=task)

    modified = False

    if form.is_valid():
        task.name = form.cleaned_data['name']
        task.description = form.cleaned_data['description']

        # The assignee field is not a part of the form.
        # We retrieve it via the POST parameter (see modify-task.html).
        assignee = User.objects.get(id=request.POST['assignee'])
        task.assignee = assignee

        task.start_date = form.cleaned_data['start_date']
        task.due_date = form.cleaned_data['due_date']
        task.priority = form.cleaned_data['priority']
        task.status = form.cleaned_data['status']

        task.save()

        modified = True

    return render(request, 'taskmanager/modify-task.html', locals())


# This view allows an user to add an entry to a task
@login_required
def add_an_entry(request, id_project, id_task):
    # Retrieves the corresponding project and task
    project = get_object_or_404(Project, id=id_project)
    task = get_object_or_404(Task, id=id_task)
    # Retrieves the user currently connected
    user = request.user
    # Create the form associated with the entry
    entry = History(task=task, author=user)

    form = HistoryForm(request.POST or None, instance=entry)

    envoi = False

    if form.is_valid():
        form.save()

        envoi = True

    return render(request, "taskmanager/create-entry.html", locals())
