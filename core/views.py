from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.core.files.storage import default_storage

from .forms import ContactForm
from .models import (
    Achievement,
    ContactMessage,
    Gallery,
    News,
    Partner,
    Project,
    Publication,
    ResearchArea,
    TeamMember,
)


def home(request):

    context = {

        "research_areas": ResearchArea.objects.all(),

        "projects": Project.objects.filter(featured=True)[:6],

        "publications": Publication.objects.filter(featured=True)[:6],

        "team_members": TeamMember.objects.filter(featured=True)[:4],

        "latest_news": News.objects.filter(featured=True)[:3],

        "total_projects": Project.objects.count(),

        "total_publications": Publication.objects.count(),

        "total_researchers": TeamMember.objects.count(),

        "total_research_areas": ResearchArea.objects.count(),

        "featured_gallery": Gallery.objects.filter(featured=True)[:8],

        "partners": Partner.objects.filter(featured=True),

        "achievements": Achievement.objects.filter(featured=True)[:6],

    }

    return render(
        request,
        "home.html",
        context,
    )


def about(request):

    return render(
        request,
        "about.html",
    )


def research(request):

    context = {

        "research_areas": ResearchArea.objects.all(),

    }

    return render(
        request,
        "research.html",
        context,
    )


def research_detail(request, slug):

    research = get_object_or_404(
        ResearchArea,
        slug=slug,
    )

    context = {

        "research": research,

    }

    return render(
        request,
        "research_detail.html",
        context,
    )


def projects(request):

    context = {

        "projects": Project.objects.all(),

    }

    return render(
        request,
        "projects.html",
        context,
    )


def project_detail(request, slug):

    project = get_object_or_404(
        Project,
        slug=slug,
    )

    related_projects = Project.objects.filter(
        category=project.category,
    ).exclude(
        id=project.id,
    )[:3]

    context = {

        "project": project,

        "related_projects": related_projects,

    }

    return render(
        request,
        "project_detail.html",
        context,
    )


def publications(request):

    context = {

        "publications": Publication.objects.all(),

    }

    return render(
        request,
        "publications.html",
        context,
    )


def publication_detail(request, pk):

    publication = get_object_or_404(
        Publication,
        pk=pk,
    )

    related_publications = Publication.objects.filter(
        journal=publication.journal,
    ).exclude(
        pk=publication.pk,
    )[:3]

    context = {

        "publication": publication,

        "related_publications": related_publications,

    }

    return render(
        request,
        "publication_detail.html",
        context,
    )


def team(request):

    context = {

        "team_members": TeamMember.objects.all(),

    }

    return render(
        request,
        "team.html",
        context,
    )


def team_detail(request, slug):

    member = get_object_or_404(
        TeamMember,
        slug=slug,
    )

    context = {

        "member": member,

    }

    return render(
        request,
        "team_detail.html",
        context,
    )


def news_detail(request, slug):

    news = get_object_or_404(
        News,
        slug=slug,
    )

    related_news = News.objects.exclude(
        id=news.id,
    )[:3]

    context = {

        "news": news,

        "related_news": related_news,

    }

    return render(
        request,
        "news_detail.html",
        context,
    )


def gallery(request):

    context = {

        "gallery": Gallery.objects.all(),

    }

    return render(
        request,
        "gallery.html",
        context,
    )


def search(request):

    query = request.GET.get(
        "q",
        "",
    )

    project_results = Project.objects.filter(
        Q(title__icontains=query) |
        Q(short_description__icontains=query)
    )

    publication_results = Publication.objects.filter(
        Q(title__icontains=query) |
        Q(authors__icontains=query)
    )

    team_results = TeamMember.objects.filter(
        Q(name__icontains=query) |
        Q(designation__icontains=query)
    )

    news_results = News.objects.filter(
        Q(title__icontains=query) |
        Q(short_description__icontains=query)
    )

    context = {

        "query": query,

        "project_results": project_results,

        "publication_results": publication_results,

        "team_results": team_results,

        "news_results": news_results,

    }

    return render(
        request,
        "search.html",
        context,
    )


def contact(request):

    if request.method == "POST":

        form = ContactForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Your message has been sent successfully.",
            )

            return redirect(
                "contact",
            )

    else:

        form = ContactForm()

    context = {

        "form": form,

    }

    return render(
        request,
        "contact.html",
        context,
    )