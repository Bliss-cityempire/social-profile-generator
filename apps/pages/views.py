from django.db import models
from django.shortcuts import get_object_or_404, render

from .models import LandingPage


def public_landing_page(request, slug):
    page = get_object_or_404(
        LandingPage.objects.select_related("profile"),
        slug=slug,
        published=True,
    )

    return render(
        request,
        "pages/public_landing_page.html",
        {
            "page": page,
            "profile": page.profile,
        },
    )

def public_directory(request):
    from apps.pages.models import LandingPage

    query = request.GET.get("q", "").strip()

    pages = LandingPage.objects.filter(
        published=True,
    ).select_related(
        "profile",
    ).order_by(
        "-updated_at",
    )

    if query:
        pages = pages.filter(
            models.Q(profile__username__icontains=query)
            | models.Q(profile__display_name__icontains=query)
            | models.Q(headline__icontains=query)
            | models.Q(slug__icontains=query)
        )

    return render(
        request,
        "pages/public_directory.html",
        {
            "pages": pages,
            "query": query,
        },
    )