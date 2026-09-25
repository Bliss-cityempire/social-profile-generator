from rest_framework import serializers

from apps.pages.models import LandingPage


class PublicSocialProfileSerializer(serializers.Serializer):
    display_name = serializers.CharField()
    username = serializers.CharField()
    bio = serializers.CharField()
    profile_image = serializers.ImageField()


class PublicLandingPageSerializer(serializers.ModelSerializer):
    profile = PublicSocialProfileSerializer(read_only=True)

    class Meta:
        model = LandingPage
        fields = (
            "slug",
            "profile",
            "headline",
            "description",
            "button_text",
            "button_url",
            "template",
        )