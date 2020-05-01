from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# This model represents a project
class Project(models.Model):
    name = models.CharField(max_length=300, verbose_name="Nom du projet")
    users = models.ManyToManyField(User, verbose_name="Participants au projet", related_name="projects")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = "projet"


# This model represents the status of a task, in a project (started, finished, ...)
class Status(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nom de la tâche")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = "statut"


# This model represents a task of a project
class Task(models.Model):
    project = models.ForeignKey(Project, verbose_name="Projet rattaché à la tâche", on_delete="CASCADE")
    name = models.CharField(max_length=500, verbose_name="Nom de la tâche")
    description = models.TextField(blank=True, verbose_name="Description de la tâche")
    assignee = models.ForeignKey(
        User,
        verbose_name="Personne réalisant la tâche",
        on_delete="CASCADE",
    )
    start_date = models.DateTimeField(default=timezone.now, verbose_name="Date de début de la tâche")
    due_date = models.DateTimeField(default=timezone.now, verbose_name="Date de rendu de la tâche")
    priority = models.IntegerField(default=0, verbose_name="Priorité de la tâche")
    status = models.ForeignKey(Status, verbose_name="Statut de la tâche", null=True, on_delete="SET_NULL")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['status']
        verbose_name = "tâche"


# This model represents the history of a task
class History(models.Model):
    date = models.DateTimeField(default=timezone.now, verbose_name="Date de l'entrée du journal")
    entry = models.TextField(verbose_name="Entrée du journal")
    author = models.ForeignKey(User, verbose_name="Auteur de l'entrée", on_delete="CASCADE")
    task = models.ForeignKey(Task, verbose_name="Tâche s'y rattachant", on_delete="CASCADE")

    def __str__(self):
        return self.entry

    class Meta:
        ordering = ['date']
        verbose_name = "entrée du journal"
        verbose_name_plural = "entrées du journal"
