from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic

from list.forms import TaskForm
from list.models import Task, Tag


def index(request):
    tasks = Task.objects.all().order_by("is_done", "-created_at")
    return render(request, "list/index.html", {"tasks": tasks})


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("list:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("list:index")


class TagsList(generic.ListView):
    model = Tag
    context_object_name = "tags"
    template_name = "list/tag_list.html"


def toggle_status(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.done = not task.done
    task.save()
    return redirect("list:index")
