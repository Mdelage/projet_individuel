from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # Login page for users, uses the generic class-based view LoginView
    path('login/', LoginView.as_view(template_name='taskmanager/login.html'), name="login"),
    # Logout page for users
    path('logout', LogoutView.as_view(), name="logout"),
    # Lists of the projects
    path('projects/', views.projects, name="view_all_projects"),
    # Lists of the tasks of a project
    path('projects/<int:id_project>/', views.tasks_of_project, name="view_tasks"),
    path('projects/<int:id_project>/tasks/', views.tasks_of_project, name="view_tasks_alt"),
    # Details of a task
    path('projects/<int:id_project>/tasks/<int:id_task>/', views.details_of_task, name="view_details"),
    # Adding a task to a project
    path('projects/<int:id_project>/newtask/', views.add_a_task, name="add_a_task"),
    # Modifying a task
    path('projects/<int:id_project>/modify-task/<int:id_task>', views.modify_a_task, name="modify_a_task"),
    # Adding an entry to a task
    path('projects/<int:id_project>/tasks/<int:id_task>/add-entry', views.add_an_entry, name="add_an_entry"),
]
