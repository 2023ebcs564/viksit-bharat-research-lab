from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def research(request):
    return render(request, "research.html")


def projects(request):
    return render(request, "projects.html")


def team(request):
    return render(request, "team.html")


def publications(request):
    return render(request, "publications.html")


def contact(request):
    return render(request, "contact.html")