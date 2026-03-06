from django.urls import path

from tasks import views

app_name = "tasks"

urlpatterns = [
    path("", views.home, name="home"),
    path("task/create/", views.task_create, name="task-create"),
    path("task/<int:pk>/delete/", views.task_delete, name="task-delete"),
    path("task/<int:pk>/update/", views.task_update, name="task-update"),
    path("task/<int:pk>/toggle/", views.task_toggle, name="task-toggle"),
    path("tags/", views.get_tags_view, name="tags-list"),
    path("tags/create/", views.tag_create, name="tags-create"),
    path("tags/<int:pk>/update", views.tag_update, name="tags-update"),
    path("tags/<int:pk>/delete", views.tag_delete, name="tags-delete"),
]
