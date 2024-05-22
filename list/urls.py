from django.urls import path

from list.views import index, TaskCreateView, TaskUpdateView, TagsList


urlpatterns = [
    path("", index, name="index"),
    path('add/', TaskCreateView.as_view(), name='task-add'),
    path('update/', TaskUpdateView.as_view(), name='task-update'),
    path('tags/', TagsList.as_view(), name='tag-list'),
]

app_name = "list"
