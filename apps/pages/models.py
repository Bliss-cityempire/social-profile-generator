import uuid

from django.db import models

from apps.profiles.models import SocialProfile


class LandingPage(models.Model):

    class Template(models.TextChoices):
        MINIMAL = "minimal", "Minimal"
        MODERN = "modern", "Modern"
        PREMIUM = "premium", "Premium"

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    profile = models.OneToOneField(
        SocialProfile,
        on_delete=models.CASCADE,
        related_name="landing_page",
    )

    slug = models.SlugField(
        max_length=50,
        unique=True,
    )

    headline = models.CharField(
        max_length=200,
        blank=True,
    )

    description = models.TextField(
        blank=True,
    )

    button_text = models.CharField(
        max_length=100,
        default="View Profile",
    )

    button_url = models.URLField(
        max_length=500,
        blank=True,
    )

    template = models.CharField(
        max_length=20,
        choices=Template.choices,
        default=Template.MODERN,
    )

    published = models.BooleanField(
        default=False,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.headline or self.slug