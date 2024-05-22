from django.shortcuts import render

from list.models import Task


def index(request):
    tasks = Task.objects.all().order_by("is_done", "-created_at")
    return render(request, "todolist/index.html", {"tasks": tasks})
