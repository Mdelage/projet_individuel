# Generated by Django 2.1.7 on 2020-04-29 10:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('taskmanager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=300, verbose_name='Nom du projet'),
        ),
    ]
