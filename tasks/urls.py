from django.urls import path
from tasks.views import task_create, show_tasks


urlpatterns = [
    path("create/", task_create, name="create_task"),
    path("mine/", show_tasks, name="show_my_tasks"),
]
