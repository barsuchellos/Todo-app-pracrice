from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from tasks.models import Task, Tag
from tasks.services import switch_toggle


class TaskListView(ListView):
    model = Task
    template_name = "tasks/home.html"
    context_object_name = 'tasks'
    ordering = ['-created_at']


class TaskCreateView(CreateView):
    model = Task
    fields = ["content", "deadline", "is_done", "tags"]
    success_url = reverse_lazy('tasks:home')


class TaskUpdateView(UpdateView):
    model = Task
    fields = ["content", "deadline", "is_done", "tags"]
    success_url = reverse_lazy('tasks:home')


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('tasks:home')


class TagListView(ListView):
    model = Tag
    template_name = "tasks/tag_list.html"
    context_object_name = 'tags'


class TagDeleteView(DeleteView):
    model = Tag
    success_url = reverse_lazy('tasks:tags-list')


class TagUpdateView(UpdateView):
    model = Tag
    fields = ["name"]
    success_url = reverse_lazy('tasks:tags-list')


class TagCreateView(CreateView):
    model = Tag
    fields = ["name"]
    success_url = reverse_lazy('tasks:tags-list')


class TaskToggleView(View):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.is_done = not task.is_done
        task.save()
        return redirect('tasks:home')
