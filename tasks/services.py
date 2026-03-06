from tasks.models import Task, Tag
from tasks.selectors import get_task, get_tag


def create_task_service(form_data):
    task = Task.objects.create(
        content=form_data["content"],
        deadline=form_data["deadline"],
        is_done=form_data["is_done"],
    )

    task.tags.set(form_data["tags"])
    return task


def delete_task(task):
    task.delete()


def update_task_service(data, task):
    task.content = data["content"]
    task.deadline = data["deadline"]
    task.is_done = data["is_done"]

    task.save()
    task.tags.set(data["tags"])


def switch_toggle(pk):
    task = get_task(pk)
    task.is_done = not task.is_done
    task.save()


def create_tag_service(form_data):
    return Tag.objects.create(
        name=form_data["name"]
    )


def update_tag_service(form_data, tag):
    tag.name = form_data["name"]
    tag.save()


def delete_tag(tag):
    tag.delete()