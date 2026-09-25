from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from apps.pages.views import (
    public_directory,
    public_landing_page,
)


urlpatterns = [
    path("admin/", admin.site.urls),

    # Authentication / accounts
    path(
        "accounts/",
        include("apps.accounts.urls"),
    ),

    # APIs
    path(
        "api/profiles/",
        include("apps.profiles.api.urls"),
    ),

    path(
        "api/pages/",
        include("apps.pages.api.urls"),
    ),

    # Public directory
    path(
        "directory/",
        public_directory,
        name="public-directory",
    ),

    # Public landing pages
    path(
        "<slug:slug>/",
        public_landing_page,
        name="public-landing-page",
    ),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )