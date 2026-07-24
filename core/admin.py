from django.contrib import admin
from django.utils.html import format_html

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
        "thumbnail",
        "featured",
        "created_at",
    )

    list_editable = (
        "featured",
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

    def thumbnail(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="height:45px;width:45px;object-fit:cover;border-radius:6px;" />',
                obj.image.url,
            )
        return "—"

    thumbnail.short_description = "Photo"


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "thumbnail",
        "category",
        "display_order",
        "featured",
        "created_at",
    )

    list_editable = (
        "display_order",
        "featured",
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

    def thumbnail(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="height:45px;width:45px;object-fit:cover;border-radius:6px;" />',
                obj.image.url,
            )
        return "—"

    thumbnail.short_description = "Photo"


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "journal",
        "year",
        "featured",
    )

    list_editable = (
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
        "thumbnail",
        "team_group",
        "display_order",
        "designation",
        "featured",
    )

    list_editable = (
        "team_group",
        "display_order",
        "featured",
    )

    list_filter = (
        "team_group",
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

    def thumbnail(self, obj):
        if obj.photo:
            return format_html(
                '<img src="{}" style="height:45px;width:45px;object-fit:cover;border-radius:50%;" />',
                obj.photo.url,
            )
        return "—"

    thumbnail.short_description = "Photo"


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "thumbnail",
        "published_date",
        "featured",
    )

    list_editable = (
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

    def thumbnail(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="height:45px;width:45px;object-fit:cover;border-radius:6px;" />',
                obj.image.url,
            )
        return "—"

    thumbnail.short_description = "Photo"


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
        "thumbnail",
        "category",
        "display_order",
        "featured",
    )

    list_editable = (
        "display_order",
        "featured",
    )

    list_filter = (
        "category",
        "featured",
    )

    search_fields = (

        "title",

    )

    def thumbnail(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="height:45px;width:45px;object-fit:cover;border-radius:6px;" />',
                obj.image.url,
            )
        return "—"

    thumbnail.short_description = "Photo"


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "thumbnail",
        "display_order",
        "featured",
    )

    list_editable = (
        "display_order",
        "featured",
    )

    list_filter = (

        "featured",

    )

    search_fields = (

        "name",

    )

    def thumbnail(self, obj):
        if obj.logo:
            return format_html(
                '<img src="{}" style="height:45px;width:45px;object-fit:contain;border-radius:6px;" />',
                obj.logo.url,
            )
        return "—"

    thumbnail.short_description = "Logo"


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "thumbnail",
        "year",
        "display_order",
        "featured",
    )

    list_editable = (
        "display_order",
        "featured",
    )

    list_filter = (
        "year",
        "featured",
    )

    search_fields = (

        "title",

    )

    def thumbnail(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="height:45px;width:45px;object-fit:cover;border-radius:6px;" />',
                obj.image.url,
            )
        return "—"

    thumbnail.short_description = "Photo"


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):

    list_display = (
        "site_name",
        "email",
        "phone",
    )


admin.site.site_header = "Viksit Bharat Research Lab Admin"
admin.site.site_title = "Research Lab Admin"
admin.site.index_title = "Administration Dashboard"