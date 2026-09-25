import uuid

from django.conf import settings
from django.db import models


class SocialProfile(models.Model):

    class Platform(models.TextChoices):
        TIKTOK = "tiktok", "TikTok"
        FACEBOOK = "facebook", "Facebook"
        INSTAGRAM = "instagram", "Instagram"
        X = "x", "X"
        LINKEDIN = "linkedin", "LinkedIn"

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="social_profiles",
    )

    platform = models.CharField(
        max_length=20,
        choices=Platform.choices,
    )

    profile_url = models.URLField(
        max_length=500,
    )

    username = models.CharField(
        max_length=150,
        blank=True,
    )

    display_name = models.CharField(
        max_length=200,
        blank=True,
    )

    bio = models.TextField(
        blank=True,
    )

    profile_image = models.ImageField(
        upload_to="profiles/",
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.display_name or self.username or self.profile_url