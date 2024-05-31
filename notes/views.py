from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from notes.models import Note
from notes.forms import NoteForm
import random


# Create your views here.
@login_required
def list_notes(request):
    notes = Note.objects.filter(owner=request.user)

    context = {
        "notes": notes,
    }

    return render(request, "notes/list_notes.html", context)


# detail view for a specific note:
@login_required
def note_detail(request, id):
    note = get_object_or_404(Note, id=id)
    colors = ["#FFF68F", "#73D949", "#F38FB7", "#62C9F6"]
    random_color = random.choice(colors)

    context = {
        "note": note,
        "background_color": random_color,
    }

    return render(request, "notes/note_detail.html", context)


# create view for new note:
@login_required
def note_create(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note_form = form.save(commit=False)
            note_form.owner = request.user
            note_form.save()
            return redirect("list_notes")

    elif request.method == "GET":
        form = NoteForm()

    context = {
        "form": form,
    }

    return render(request, "notes/note_create.html", context)


# view for editing a particular note:
@login_required
def note_edit(request, id):
    n_edit = get_object_or_404(Note, id=id)

    if request.method == "POST":
        form = NoteForm(request.POST, instance=n_edit)
        if form.is_valid():
            edited_note = form.save(commit=False)
            edited_note.owner = request.user
            edited_note.save()
            return redirect("note_detail", id=n_edit.id)

    elif request.method == "GET":
        form = NoteForm(instance=n_edit)

    context = {
        "form": form,
    }

    return render(request, "notes/note_edit.html", context)
