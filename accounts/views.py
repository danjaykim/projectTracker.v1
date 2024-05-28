from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from accounts.forms import LoginForm

# Create your views here.


# views for login:
def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(
                request,
                username=username,
                password=password,
            )

            if user is not None:
                login(request, user)
                return redirect("list_projects")

    elif request.method == "GET":
        form = LoginForm()

    context = {
        "form": form,
    }

    return render(request, "accounts/login.html", context)


# views for logging out:
def user_logout(request):
    logout(request)
    return redirect("login")
