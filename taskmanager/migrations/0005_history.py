# Generated by Django 2.1.7 on 2020-04-30 07:41

from django.conf import settings
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taskmanager', '0004_auto_20200430_0642'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date',
                 models.DateTimeField(default=django.utils.timezone.now, verbose_name="Date de l'entrée du journal")),
                ('entry', models.TextField(verbose_name='Entrée du journal')),
                ('author', models.ForeignKey(on_delete='CASCADE', to=settings.AUTH_USER_MODEL,
                                             verbose_name="Auteur de l'entrée")),
                ('task',
                 models.ForeignKey(on_delete='CASCADE', to='taskmanager.Task', verbose_name="Tâche s'y rattachant")),
            ],
            options={
                'verbose_name': 'entrée du journal',
                'verbose_name_plural': 'entrées du journal',
                'ordering': ['date'],
            },
        ),
    ]
