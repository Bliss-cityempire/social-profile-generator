from django.urls import path

from .views import (
    dashboard_view,
    landing_page_manage_view,
    login_view,
    logout_view,
    profile_create_view,
    profile_manage_view,
    signup_view,
)


urlpatterns = [
    path("login/", login_view, name="login"),
    path("signup/", signup_view, name="signup"),
    path("logout/", logout_view, name="logout"),
    path("dashboard/", dashboard_view, name="dashboard"),

    path(
        "profiles/new/",
        profile_create_view,
        name="profile-create",
    ),

    path(
        "profiles/<uuid:profile_id>/",
        profile_manage_view,
        name="profile-manage",
    ),

    path(
        "pages/<uuid:page_id>/",
        landing_page_manage_view,
        name="landing-page-manage",
    ),
]