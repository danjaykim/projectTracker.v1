from django.shortcuts import render

# Create your views here.


def homepage(request):
    return render(request, "homes/home.html")


def contact(request):
    return render(request, "homes/contact.html")


def about(request):
    return render(request, "homes/about.html")
