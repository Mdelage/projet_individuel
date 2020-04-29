from django.shortcuts import render


# This view displays all the projects
def projects(request):
    return render(request, "taskmanager/projects.html", locals())
