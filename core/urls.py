from django.urls import path
from django.contrib.sitemaps.views import sitemap

from .sitemaps import (
    StaticViewSitemap,
    ResearchAreaSitemap,
    ProjectSitemap,
    PublicationSitemap,
    TeamMemberSitemap,
    NewsSitemap,
)

sitemaps = {
    "static": StaticViewSitemap,
    "research": ResearchAreaSitemap,
    "projects": ProjectSitemap,
    "publications": PublicationSitemap,
    "team": TeamMemberSitemap,
    "news": NewsSitemap,
}
from . import views

urlpatterns = [

 path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="sitemap",
    ),

    path(
        "robots.txt",
        views.robots_txt,
        name="robots_txt",
    ),

    path(
        "",
        views.home,
        name="home",
    ),

    path(
        "about/",
        views.about,
        name="about",
    ),

    path(
        "research/",
        views.research,
        name="research",
    ),

    path(
        "research/<slug:slug>/",
        views.research_detail,
        name="research_detail",
    ),

    path(
        "projects/",
        views.projects,
        name="projects",
    ),

    path(
        "projects/<slug:slug>/",
        views.project_detail,
        name="project_detail",
    ),

    path(
        "publications/",
        views.publications,
        name="publications",
    ),

    path(
        "publications/<int:pk>/",
        views.publication_detail,
        name="publication_detail",
    ),

    path(
        "team/",
        views.team,
        name="team",
    ),

    path(
        "team/<slug:slug>/",
        views.team_detail,
        name="team_detail",
    ),

    path(
        "gallery/",
        views.gallery,
        name="gallery",
    ),

    path(
        "contact/",
        views.contact,
        name="contact",
    ),

    path(
        "search/",
        views.search,
        name="search",
    ),

    path(
        "news/<slug:slug>/",
        views.news_detail,
        name="news_detail",
    ),

]