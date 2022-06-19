# flake8: noqa
# Generated by Django 4.0.4 on 2022-06-13 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0001_initial'),
        ('tasks', '0002_alter_task_label'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='label',
            field=models.ManyToManyField(blank=True, null=True, related_name='tasks', through='tasks.LabelTaskIntermediate', to='labels.label', verbose_name='Label'),
        ),
    ]
