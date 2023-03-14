from django.urls import path

from manager.views import index, PositionListView, TaskTypeListView, WorkerListView, TaskListView, TaskDetailView, WorkerDetailView, PositionDetailView, TaskTypeDetailView

urlpatterns = [
    path("", index, name="index"),

    path("positions/", PositionListView.as_view(), name="position-list"),
    path("task-types/", TaskTypeListView.as_view(), name="task-type-list"),
    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path("tasks/", TaskListView.as_view(), name="task-list"),

    path("tasks/<int:pk>", TaskDetailView.as_view(), name="task-detail"),
    path("workers/<int:pk>", WorkerDetailView.as_view(), name="worker-detail"),
    path("position/<int:pk>", PositionDetailView.as_view(), name="position-detail"),
    path("task-types/<int:pk>", TaskTypeDetailView.as_view(), name="task-type-detail"),
]

app_name = "manager"
