# Generated by Django 4.1.7 on 2023-03-13 16:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("manager", "0002_alter_worker_position"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="assignees",
            field=models.ManyToManyField(
                related_name="tasks", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="task",
            name="task_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tasks",
                to="manager.tasktype",
            ),
        ),
    ]
