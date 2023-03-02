from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(to=Position, on_delete=models.CASCADE, related_name="workers")

    class Meta:
        ordering = ["username"]


class TaskType(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Task(models.Model):
    PRIORITY_CHOICES = (
        ("4", "critical"),
        ("3", "high"),
        ("2", "medium"),
        ("1", "low"),
    )

    name = models.CharField(max_length=64)
    description = models.TextField()
    deadline = models.DateField()
    is_completed = models.BooleanField()
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES)
    task_type = models.ForeignKey(to=TaskType, on_delete=models.CASCADE)
    assignees = models.ManyToManyField(to=settings.AUTH_USER_MODEL)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        if self.is_completed:
            return f"{self.name} is completed"
        return f"{self.name} is still in progress"
