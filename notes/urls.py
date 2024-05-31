from django.urls import path
from notes.views import list_notes, note_detail, note_create


urlpatterns = [
    path("", list_notes, name="list_notes"),
    path("<int:id>/", note_detail, name="note_detail"),
    path("create/", note_create, name="note_create"),
]
