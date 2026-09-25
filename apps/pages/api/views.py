from rest_framework import generics

from apps.pages.models import LandingPage

from .serializers import LandingPageSerializer


class LandingPageListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = LandingPageSerializer

    def get_queryset(self):
        return LandingPage.objects.filter(
            profile__user=self.request.user
        )


class LandingPageDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LandingPageSerializer

    def get_queryset(self):
        return LandingPage.objects.filter(
            profile__user=self.request.user
        )