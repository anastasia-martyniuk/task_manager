from django.urls import path

from manager.views import index, PositionListView, TaskTypeListView

urlpatterns = [
    path("", index, name="index"),
    path("positions/", PositionListView.as_view(), name="position-list"),
    path("task-types", TaskTypeListView.as_view(), name="task-type-list"),
]

app_name = "manager"
