from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from notes.models import Note
from notes.forms import NoteForm


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

    context = {
        "note": note,
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
