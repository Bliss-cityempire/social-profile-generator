from rest_framework import generics
from rest_framework.permissions import AllowAny

from apps.pages.models import LandingPage

from .public_serializers import PublicLandingPageSerializer


class PublicLandingPageAPIView(generics.RetrieveAPIView):
    serializer_class = PublicLandingPageSerializer
    permission_classes = [AllowAny]
    lookup_field = "slug"

    def get_queryset(self):
        return LandingPage.objects.filter(
            published=True
        )