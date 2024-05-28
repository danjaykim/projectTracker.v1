from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from tasks.forms import TaskForm

# Create your views here.


# views for creating a task:
@login_required
def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_projects")

    elif request.method == "GET":
        form = TaskForm()

    context = {
        "form": form,
    }

    return render(request, "tasks/task_create.html", context)
