from django.urls import path

from list.views import (
    index,
    TaskCreateView,
    TaskUpdateView,
    TagsList,
    TagCreateView,
    TagsUpdateView,
    toggle_status)


urlpatterns = [
    path("", index, name="index"),
    path('tasks/add/', TaskCreateView.as_view(), name='task-add'),
    path('tasks/<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
    path('tags/', TagsList.as_view(), name='tag-list'),
    path('tags/add/', TagCreateView.as_view(), name='tag-add'),
    path('tags/<int:pk>/update/', TagsUpdateView.as_view(), name='tag-update'),
    path('toggle/<int:task_id>/', toggle_status, name='toggle-status'),
]

app_name = "list"
