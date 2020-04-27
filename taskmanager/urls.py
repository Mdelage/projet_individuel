from django.urls import path
from . import views

urlpatterns = [
    # Login pages for users
    path('login/', views.login, name="login"),
]
