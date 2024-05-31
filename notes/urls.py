from django.urls import path
from notes.views import list_notes, note_detail, note_create, note_edit


urlpatterns = [
    path("", list_notes, name="list_notes"),
    path("<int:id>/", note_detail, name="note_detail"),
    path("<int:id>/edit/", note_edit, name="note_edit"),
    path("create/", note_create, name="note_create"),
]
