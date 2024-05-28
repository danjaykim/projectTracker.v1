from django.shortcuts import render
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
