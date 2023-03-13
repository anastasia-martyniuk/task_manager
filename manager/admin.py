from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from manager.models import Position, Worker, TaskType, Task

admin.site.register(Position)
admin.site.register(Worker, UserAdmin)
admin.site.register(TaskType)
admin.site.register(Task)
