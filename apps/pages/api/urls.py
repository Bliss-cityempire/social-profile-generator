from django.urls import path

from .public_views import PublicLandingPageAPIView
from .views import (
    LandingPageDetailAPIView,
    LandingPageListCreateAPIView,
)


urlpatterns = [
    path(
        "",
        LandingPageListCreateAPIView.as_view(),
        name="landing-page-list-create",
    ),
    path(
        "<uuid:pk>/",
        LandingPageDetailAPIView.as_view(),
        name="landing-page-detail",
    ),
    path(
        "public/<slug:slug>/",
        PublicLandingPageAPIView.as_view(),
        name="public-landing-page",
    ),
]