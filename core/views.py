import requests

from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.core.files.storage import default_storage
from django.conf import settings

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


TEAM_GROUP_ORDER = [
    "Leadership",
    "Research Team",
    "Technical Team",
    "Advisory Board",
]


def send_brevo_email(to_email, to_name, subject, text_content):

    try:
        response = requests.post(
            "https://api.brevo.com/v3/smtp/email",
            headers={
                "accept": "application/json",
                "api-key": settings.BREVO_API_KEY,
                "content-type": "application/json",
            },
            json={
                "sender": {
                    "name": settings.BREVO_SENDER_NAME,
                    "email": settings.BREVO_SENDER_EMAIL,
                },
                "to": [
                    {"email": to_email, "name": to_name},
                ],
                "subject": subject,
                "textContent": text_content,
            },
            timeout=10,
        )
        print(f"BREVO STATUS: {response.status_code}")
        print(f"BREVO RESPONSE: {response.text}")
    except requests.RequestException as e:
        print(f"BREVO EXCEPTION: {e}")


def debug_storage(request):

    info = f"""
    Storage Class: {default_storage.__class__}
    Module: {default_storage.__class__.__module__}
    """

    return HttpResponse(f"<pre>{info}</pre>")


def home(request):

    featured_members = TeamMember.objects.filter(featured=True)

    home_grouped_team = []

    for group_name in TEAM_GROUP_ORDER:

        group_members = featured_members.filter(team_group=group_name)[:4]

        if group_members.exists():
            home_grouped_team.append(
                {
                    "name": group_name,
                    "members": group_members,
                }
            )

    context = {

        "research_areas": ResearchArea.objects.all(),

        "projects": Project.objects.filter(featured=True)[:6],

        "publications": Publication.objects.filter(featured=True)[:6],

        "home_grouped_team": home_grouped_team,

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

    all_members = TeamMember.objects.all()

    grouped_team = []

    for group_name in TEAM_GROUP_ORDER:

        group_members = all_members.filter(team_group=group_name)

        if group_members.exists():
            grouped_team.append(
                {
                    "name": group_name,
                    "members": group_members,
                }
            )

    context = {

        "grouped_team": grouped_team,

        "team_members": all_members,

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

            contact_message = form.save()

            send_brevo_email(
                to_email=settings.ADMIN_EMAIL,
                to_name="Admin",
                subject=f"New Contact Message: {contact_message.subject}",
                text_content=(
                    f"Name: {contact_message.name}\n"
                    f"Email: {contact_message.email}\n\n"
                    f"Message:\n{contact_message.message}"
                ),
            )

            send_brevo_email(
                to_email=contact_message.email,
                to_name=contact_message.name,
                subject="We've received your message - Viksit Bharat Research Lab",
                text_content=(
                    f"Hi {contact_message.name},\n\n"
                    "Thank you for reaching out to Viksit Bharat Research Lab. "
                    "We've received your message and will get back to you soon.\n\n"
                    "Your message:\n"
                    f"{contact_message.message}\n\n"
                    "Regards,\n"
                    "Viksit Bharat Research Lab"
                ),
            )

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


def robots_txt(request):

    lines = [
        "User-agent: *",
        "Allow: /",
        "Disallow: /admin/",
        "",
        f"Sitemap: {request.scheme}://{request.get_host()}/sitemap.xml",
    ]

    return HttpResponse(
        "\n".join(lines),
        content_type="text/plain",
    )