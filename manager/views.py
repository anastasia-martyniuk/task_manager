from django.shortcuts import render
from django.views import generic

from manager.models import Position, Worker, TaskType, Task


def index(request):
    num_positions = Position.objects.count()
    num_workers = Worker.objects.count()
    num_tasks_type = TaskType.objects.count()
    num_tasks = Task.objects.count()

    context = {
        "num_positions": num_positions,
        "num_workers": num_workers,
        "num_tasks_type": num_tasks_type,
        "num_tasks": num_tasks,
    }

    return render(request, "manager/index.html", context=context)


class PositionListView(generic.ListView):
    model = Position


class TaskTypeListView(generic.ListView):
    model = TaskType
    template_name = "manager/task_type_list.html"
    context_object_name = "task-type-list"
