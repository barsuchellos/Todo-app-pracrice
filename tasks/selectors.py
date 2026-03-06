from tasks.models import Task, Tag


def get_all_tasks():
    return Task.objects.order_by("is_done", "-created_at")

def get_all_tasks_count():
    return Task.objects.all().count()

def get_all_not_done_tasks_count():
    return Task.objects.filter(is_done=False).count()

def get_task(pk):
    return Task.objects.get(pk=pk)


def get_tags():
    return Tag.objects.all()


def get_tag(pk):
    return Tag.objects.get(pk=pk)
