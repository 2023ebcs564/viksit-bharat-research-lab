from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import (
    ResearchArea,
    Project,
    Publication,
    TeamMember,
    News,
)


class StaticViewSitemap(Sitemap):

    priority = 0.8
    changefreq = "monthly"

    def items(self):
        return [
            "home",
            "about",
            "research",
            "projects",
            "publications",
            "team",
            "gallery",
            "contact",
        ]

    def location(self, item):
        return reverse(item)


class ResearchAreaSitemap(Sitemap):

    priority = 0.7
    changefreq = "monthly"

    def items(self):
        return ResearchArea.objects.all()

    def location(self, obj):
        return reverse("research_detail", args=[obj.slug])


class ProjectSitemap(Sitemap):

    priority = 0.7
    changefreq = "monthly"

    def items(self):
        return Project.objects.all()

    def lastmod(self, obj):
        return obj.created_at

    def location(self, obj):
        return reverse("project_detail", args=[obj.slug])


class PublicationSitemap(Sitemap):

    priority = 0.6
    changefreq = "yearly"

    def items(self):
        return Publication.objects.all()

    def lastmod(self, obj):
        return obj.created_at

    def location(self, obj):
        return reverse("publication_detail", args=[obj.pk])


class TeamMemberSitemap(Sitemap):

    priority = 0.6
    changefreq = "monthly"

    def items(self):
        return TeamMember.objects.exclude(slug="")

    def location(self, obj):
        return reverse("team_detail", args=[obj.slug])


class NewsSitemap(Sitemap):

    priority = 0.6
    changefreq = "weekly"

    def items(self):
        return News.objects.all()

    def lastmod(self, obj):
        return obj.created_at

    def location(self, obj):
        return reverse("news_detail", args=[obj.slug])