from rest_framework import serializers

from apps.profiles.models import SocialProfile


class SocialProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialProfile
        fields = (
            "id",
            "platform",
            "profile_url",
            "username",
            "display_name",
            "bio",
            "profile_image",
            "created_at",
            "updated_at",
        )
        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
        )