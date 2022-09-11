from django.urls import path

import tasks.views
from .views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
    change_task_status
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("add/", TaskCreateView.as_view(), name="task-add"),
    path("<int:pk>", change_task_status, name="change-task-status"),
    path("<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/add", TagCreateView.as_view(), name="tag-add"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),

]

app_name = "tasks"
