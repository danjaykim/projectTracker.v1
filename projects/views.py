from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from projects.models import Project
from projects.forms import ProjectForm

# Create your views here.


# views for all instances of the Project model:
@login_required
def list_projects(request):
    project_list = Project.objects.filter(owner=request.user)

    context = {
        "project_list": project_list,
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
