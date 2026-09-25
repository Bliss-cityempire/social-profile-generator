from django.contrib import admin

from .models import SocialProfile


@admin.register(SocialProfile)
class SocialProfileAdmin(admin.ModelAdmin):
    list_display = (
        "display_name",
        "username",
        "platform",
        "user",
        "created_at",
    )
    list_filter = ("platform", "created_at")
    search_fields = ("display_name", "username", "profile_url")