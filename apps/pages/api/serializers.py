from rest_framework import serializers

from apps.pages.models import LandingPage


class LandingPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandingPage
        fields = (
            "id",
            "profile",
            "slug",
            "headline",
            "description",
            "button_text",
            "button_url",
            "template",
            "published",
            "created_at",
            "updated_at",
        )
        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
        )

    def validate_profile(self, profile):
        request = self.context.get("request")

        if request is None or not request.user.is_authenticated:
            raise serializers.ValidationError(
                "Authentication is required."
            )

        if profile.user_id != request.user.id:
            raise serializers.ValidationError(
                "You can only create a landing page for your own profile."
            )

        return profile
