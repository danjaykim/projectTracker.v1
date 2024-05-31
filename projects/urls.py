from django.urls import path
from projects.views import (
    list_projects,
    project_detail,
    project_create,
)


urlpatterns = [
    path("", list_projects, name="list_projects"),
    path("<int:id>/", project_detail, name="show_project"),
    path("create/", project_create, name="create_project"),
]
