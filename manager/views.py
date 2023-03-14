from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from manager.forms import TaskTypeForm
from manager.models import Position, Worker, TaskType, Task


def index(request):
    num_positions = Position.objects.count()
    num_workers = Worker.objects.count()
    num_tasks_type = TaskType.objects.count()
    num_tasks = Task.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    if 'last_visit' in request.session:
        last_visit = request.session['last_visit']
        last_visit = datetime.fromtimestamp(last_visit)

    else:
        last_visit = datetime.now()

    request.session['last_visit'] = last_visit.timestamp()

    context = {
        "num_positions": num_positions,
        "num_workers": num_workers,
        "num_tasks_type": num_tasks_type,
        "num_tasks": num_tasks,
        "num_visits": num_visits + 1,
        "last_visit": last_visit
    }

    return render(request, "manager/index.html", context=context)


class PositionListView(LoginRequiredMixin, generic.ListView):
    model = Position
    paginate_by = 10


class TaskTypeListView(LoginRequiredMixin, generic.ListView):
    model = TaskType
    template_name = "manager/task_type_list.html"
    context_object_name = "task_type_list"
    paginate_by = 10


class WorkerListView(LoginRequiredMixin, generic.ListView):
    model = Worker
    paginate_by = 10


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    queryset = Task.objects.all().select_related("task_type")
    paginate_by = 10


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Worker


class PositionDetailView(LoginRequiredMixin, generic.DetailView):
    model = Position


class TaskTypeDetailView(LoginRequiredMixin, generic.DetailView):
    model = TaskType
    template_name = "manager/task_type_detail.html"
    context_object_name = "task_type"


def task_type_create_view(request):
    # if request.method == "GET":
    #     context = {
    #         "form": TaskTypeForm()
    #     }
    #     return render(request, "manager/task_type_form.html", context)
    #
    # elif request.method == "POST":
    #     form = TaskTypeForm(request.POST)
    #
    #     if form.is_valid:
    #         TaskType.objects.create(**form.cleaned_data)
    #         return HttpResponseRedirect(reverse("manager:task-type-list"))
    #
    #     context = {
    #         "error": "Please, provide name"
    #     }
    #
    #     return render(request, "manager/task_type_form.html", context)

    context = {}
    form = TaskTypeForm(request.POST or None)

    if form.is_valid():
        form.save()
        # TaskType.objects.create(**form.cleaned_data)
        return HttpResponseRedirect(reverse("manager:task-type-list"))

    context["form"] = form
    return render(request, "manager/task_type_form.html", context)

