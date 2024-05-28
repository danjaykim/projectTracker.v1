from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from projects.models import Project

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
