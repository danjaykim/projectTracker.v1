from django.urls import path
from tasks.views import task_create


urlpatterns = [
    path("create/", task_create, name="create_task"),
]
