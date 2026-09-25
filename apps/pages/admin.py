from django.contrib import admin

from .models import LandingPage


@admin.register(LandingPage)
class LandingPageAdmin(admin.ModelAdmin):
    list_display = (
        "headline",
        "slug",
        "profile",
        "template",
        "published",
        "created_at",
    )
    list_filter = ("template", "published", "created_at")
    search_fields = ("headline", "slug", "description")