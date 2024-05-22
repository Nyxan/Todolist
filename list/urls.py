from django.urls import path

from list.views import index, TaskCreateView, TaskUpdateView


urlpatterns = [
    path("", index, name="index"),
    path('add/', TaskCreateView.as_view(), name='task-add'),
    path('update/', TaskUpdateView.as_view(), name='task-update'),
]

app_name = "list"
