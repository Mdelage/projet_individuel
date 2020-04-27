from django.shortcuts import render


# This view allows users to log in
def login(request):
    return render(request, 'taskmanager/login.html', locals())
