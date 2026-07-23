from django.contrib import admin

from .models import (
    ResearchArea,
    Project,
    Publication,
    TeamMember,
    News,
    ContactMessage,
    Gallery,
    Partner,
    Achievement,
    SiteSettings,
)


@admin.register(ResearchArea)
class ResearchAreaAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "featured",
        "created_at",
    )

    list_filter = (
        "featured",
        "created_at",
    )

    search_fields = (
        "title",
        "short_description",
    )

    prepopulated_fields = {

        "slug": ("title",),

    }

    ordering = (

        "title",

    )


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "category",
        "featured",
        "created_at",
    )

    list_filter = (
        "category",
        "featured",
        "created_at",
    )

    search_fields = (
        "title",
        "short_description",
    )

    prepopulated_fields = {

        "slug": ("title",),

    }

    autocomplete_fields = (

        "category",

    )


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "journal",
        "year",
        "featured",
    )

    list_filter = (
        "year",
        "featured",
    )

    search_fields = (
        "title",
        "authors",
        "journal",
    )


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "designation",
        "featured",
    )

    list_filter = (
        "designation",
        "featured",
    )

    search_fields = (
        "name",
        "designation",
    )

    prepopulated_fields = {

        "slug": ("name",),

    }


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "published_date",
        "featured",
    )

    list_filter = (
        "featured",
        "published_date",
    )

    search_fields = (
        "title",
        "short_description",
    )

    prepopulated_fields = {

        "slug": ("title",),

    }


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "email",
        "subject",
        "created_at",
    )

    search_fields = (
        "name",
        "email",
        "subject",
    )

    readonly_fields = (

        "created_at",

    )


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "category",
        "featured",
    )

    list_filter = (
        "category",
        "featured",
    )

    search_fields = (

        "title",

    )


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "featured",
    )

    list_filter = (

        "featured",

    )

    search_fields = (

        "name",

    )


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "year",
        "featured",
    )

    list_filter = (
        "year",
        "featured",
    )

    search_fields = (

        "title",

    )

    admin.site.site_header = "Viksit Bharat Research Lab Admin"

admin.site.site_title = "Research Lab Admin"

admin.site.index_title = "Administration Dashboard"


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):

    list_display = (
        "site_name",
        "email",
        "phone",
    )