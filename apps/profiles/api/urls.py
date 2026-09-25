from django.urls import path

from .views import (
    SocialProfileDetailAPIView,
    SocialProfileListCreateAPIView,
)


urlpatterns = [
    path(
        "",
        SocialProfileListCreateAPIView.as_view(),
        name="social-profile-list-create",
    ),
    path(
        "<uuid:pk>/",
        SocialProfileDetailAPIView.as_view(),
        name="social-profile-detail",
    ),
]