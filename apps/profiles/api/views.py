from django.db import transaction
from rest_framework import generics

from apps.pages.models import LandingPage
from apps.profiles.models import SocialProfile

from .serializers import SocialProfileSerializer


class SocialProfileListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = SocialProfileSerializer

    def get_queryset(self):
        return SocialProfile.objects.filter(
            user=self.request.user
        )

    def perform_create(self, serializer):
        with transaction.atomic():
            profile = serializer.save(user=self.request.user)

            LandingPage.objects.create(
                profile=profile,
                slug=profile.username,
                headline=profile.display_name,
                description="Welcome to my page.",
                button_text="View Profile",
                button_url=profile.profile_url,
                template=LandingPage.Template.MODERN,
                published=True,
            )


class SocialProfileDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SocialProfileSerializer

    def get_queryset(self):
        return SocialProfile.objects.filter(
            user=self.request.user
        )