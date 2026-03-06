from django.forms import ModelForm

from tasks.models import Tag, Task


class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["content", "deadline", "is_done", "tags"]
