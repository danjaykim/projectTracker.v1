from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from projects.models import Project
from projects.forms import ProjectForm
from notes.models import Note
from projects.quotes import motivational_quotes
import random

# Create your views here.


# views for all instances of the Project model:
@login_required
def list_projects(request):
    project_list = Project.objects.filter(owner=request.user)
    notes = Note.objects.filter(owner=request.user)
    random_quote = random.choice(motivational_quotes)

    context = {
        "project_list": project_list,
        "notes": notes,
        "random_quote": random_quote,
    }

    return render(request, "projects/list.html", context)


# views for the detail of a specific project:
@login_required
def project_detail(request, id):
    project = get_object_or_404(Project, id=id)

    context = {
        "project": project,
    }

    return render(request, "projects/detail.html", context)


# views for creating a new project:
@login_required
def project_create(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project_form = form.save(commit=False)
            project_form.owner = request.user
            project_form.save()
            return redirect("list_projects")

    elif request.method == "GET":
        form = ProjectForm()

    context = {
        "form": form,
    }

    return render(request, "projects/create.html", context)


# views for editing a project:
@login_required
def project_edit(request, id):
    edit = get_object_or_404(Project, id=id)

    if request.method == "POST":
        form = ProjectForm(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return redirect("show_project", id=edit.id)

    elif request.method == "GET":
        form = ProjectForm(instance=edit)

    context = {
        "form": form,
    }

    return render(request, "projects/edit.html", context)
