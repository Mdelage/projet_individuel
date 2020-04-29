from django.db import models
from django.contrib.auth.models import User


# This model represents a project
class Project(models.Model):
    name = models.CharField(max_length=300, verbose_name="Nom du projet")
    users = models.ManyToManyField(User, verbose_name="Participants au projet", related_name="projects")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = "projet"
