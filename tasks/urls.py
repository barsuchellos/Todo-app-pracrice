from django.urls import path

from tasks import views

app_name = "tasks"

urlpatterns = [
    path("", views.TaskListView.as_view(), name="home"),
    path("task/create/", views.TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/delete/", views.TaskDeleteView.as_view(), name="task-delete"),
    path("task/<int:pk>/update/", views.TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/toggle/", views.TaskToggleView.as_view(), name="task-toggle"),
    path("tags/", views.TagListView.as_view(), name="tags-list"),
    path("tags/create/", views.TagCreateView.as_view(), name="tags-create"),
    path("tags/<int:pk>/update", views.TagUpdateView.as_view(), name="tags-update"),
    path("tags/<int:pk>/delete", views.TagDeleteView.as_view(), name="tags-delete"),
]
