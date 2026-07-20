from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("research/", views.research, name="research"),
    path("projects/", views.projects, name="projects"),
    path("team/", views.team, name="team"),
    path("publications/", views.publications, name="publications"),
    path("contact/", views.contact, name="contact"),
]