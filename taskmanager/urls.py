from django.urls import path
from . import views

urlpatterns = [
    # Login page for users
    path('login/', views.login, name="login"),
]
