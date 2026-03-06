from django.shortcuts import render, redirect

from tasks.forms import TaskForm, TagForm
from tasks.selectors import get_all_tasks, get_all_tasks_count, get_all_not_done_tasks_count, get_task, get_tags, \
    get_tag
from tasks.services import create_task_service, delete_task, update_task_service, switch_toggle, create_tag_service, \
    update_tag_service, delete_tag


def home(request):
    context = {
        "tasks": get_all_tasks(),
    }
    return render(request, "tasks/home.html", context=context)


def task_create(request):
    form = TaskForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        create_task_service(form.cleaned_data)
        return redirect("tasks:home")
    return render(request, "tasks/task_form.html", {"form": form})


def task_delete(request, pk):
    task = get_task(pk)
    if request.method == "POST":
        delete_task(task)
        return redirect("tasks:home")
    else:
        return render(request, "tasks/task_confirm_delete.html", {"task": task})


def task_update(request, pk):
    task = get_task(pk)
    form = TaskForm(request.POST or None, instance=task)
    if request.method == "POST" and form.is_valid():
        update_task_service(form.cleaned_data, task)
        return redirect("tasks:home")
    return render(request, "tasks/task_form.html", {"form": form})


def task_toggle(request, pk):
    switch_toggle(pk)
    return redirect("tasks:home")


def get_tags_view(request):
    context = {"tags": get_tags()}
    return render(request, "tasks/tag_list.html", context=context)


def tag_create(request):
    form = TagForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        create_tag_service(form.cleaned_data)
        return redirect("tasks:tags-list")
    return render(request, "tasks/tag_form.html", {"form": form})


def tag_update(request, pk):
    tag = get_tag(pk)
    form = TagForm(request.POST or None, instance=tag)
    if request.method == "POST" and form.is_valid():
        update_tag_service(form.cleaned_data, tag)
        return redirect("tasks:tags-list")
    return render(request, "tasks/tag_form.html", {"form": form})


def tag_delete(request, pk):
    tag = get_tag(pk)
    if request.method == "POST":
        delete_tag(tag)
        return redirect("tasks:tags-list")
    else:
        return render(request, "tasks/tag_confirm_delete.html", {"tag": tag})
