from django.urls import path

from manager.views import index, PositionListView, TaskTypeListView, WorkerListView, TaskListView, task_detail_view

urlpatterns = [
    path("", index, name="index"),

    path("positions/", PositionListView.as_view(), name="position-list"),
    path("task-types/", TaskTypeListView.as_view(), name="task-type-list"),
    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path("tasks/", TaskListView.as_view(), name="task-list"),

    path("tasks/<int:pk>", task_detail_view, name="task-detail"),
]

app_name = "manager"
