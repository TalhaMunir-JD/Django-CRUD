# Generated by Django 5.0.3 on 2024-03-25 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_remove_task_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.CharField(default='Default description', max_length=500),
        ),
    ]
