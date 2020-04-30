from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    # Login page for users, uses the generic class-based view LoginView
    path('login/', LoginView.as_view(template_name='taskmanager/login.html'), name="login"),
    # Lists of the projects
    path('projects/', views.projects, name="view_all_projects"),
    # Lists of the tasks of a project
    path('projects/<int:id_project>/', views.tasks_of_project, name="view_tasks"),
    path('projects/<int:id_project>/tasks/', views.tasks_of_project, name="view_tasks_alt"),
    # Details of a task
    path('projects/<int:id_project>/tasks/<int:id_task>/', views.details_of_task, name="view_details"),
]
