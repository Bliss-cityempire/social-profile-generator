from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.text import slugify

from apps.profiles.forms import SocialProfileForm
from .forms import LandingPageForm, SignUpForm

from .forms import LandingPageForm

def login_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    error = None

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")

        user = authenticate(
            request,
            username=username,
            password=password,
        )

        if user is not None:
            login(request, user)
            return redirect("dashboard")

        error = "Invalid username or password."

    return render(
        request,
        "accounts/login.html",
        {"error": error},
    )

def signup_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard")
    else:
        form = SignUpForm()

    return render(
        request,
        "accounts/signup.html",
        {
            "form": form,
        },
    )

@login_required
def logout_view(request):
    logout(request)
    return redirect("login")

@login_required
def dashboard_view(request):
    from apps.profiles.models import SocialProfile
    from apps.pages.models import LandingPage

    profiles = SocialProfile.objects.filter(
        user=request.user
    ).order_by("-created_at")

    pages = LandingPage.objects.filter(
        profile__user=request.user
    ).select_related("profile").order_by("-created_at")

    published_page_count = pages.filter(
        published=True
    ).count()

    context = {
        "profiles": profiles,
        "pages": pages,
        "profile_count": profiles.count(),
        "page_count": pages.count(),
        "published_page_count": published_page_count,
    }

    return render(
        request,
        "accounts/dashboard.html",
        context,
    )

def generate_unique_page_slug(value, profile_id=None):
    base_slug = slugify(value) or str(profile_id)[:8]

    slug = base_slug
    counter = 2

    while LandingPage.objects.filter(slug=slug).exists():
        slug = f"{base_slug}-{counter}"
        counter += 1

    return slug

@login_required
def profile_create_view(request):
    if request.method == "POST":
        form = SocialProfileForm(request.POST, request.FILES)

        if form.is_valid():
            with transaction.atomic():
                profile = form.save(commit=False)
                profile.user = request.user
                profile.save()

                page_slug = generate_unique_page_slug(
                    profile.username,
                    profile.id,
                )

                LandingPage.objects.create(
                    profile=profile,
                    slug=page_slug,
                    headline=profile.display_name or profile.username,
                    description=profile.bio,
                    button_text="View Profile",
                    button_url=profile.profile_url,
                    template=LandingPage.Template.MODERN,
                    published=True,
                )

            return redirect(
                "profile-manage",
                profile_id=profile.id,
            )
    else:
        form = SocialProfileForm()

    return render(
        request,
        "accounts/profile_create.html",
        {
            "form": form,
        },
    )

@login_required
def profile_manage_view(request, profile_id):
    from apps.profiles.models import SocialProfile

    profile = get_object_or_404(
        SocialProfile,
        id=profile_id,
        user=request.user,
    )

    if request.method == "POST":
        profile.platform = request.POST.get("platform", profile.platform)
        profile.profile_url = request.POST.get(
            "profile_url",
            profile.profile_url,
        )
        profile.username = request.POST.get(
            "username",
            profile.username,
        )
        profile.display_name = request.POST.get(
            "display_name",
            profile.display_name,
        )
        profile.bio = request.POST.get(
            "bio",
            profile.bio,
        )

        if request.FILES.get("profile_image"):
            profile.profile_image = request.FILES["profile_image"]

        profile.save()

        return redirect(
            "profile-manage",
            profile_id=profile.id,
        )

    return render(
        request,
        "accounts/profile_manage.html",
        {
            "profile": profile,
        },
    )

@login_required
def landing_page_manage_view(request, page_id):
    page = get_object_or_404(
        LandingPage.objects.select_related("profile"),
        id=page_id,
        profile__user=request.user,
    )

    if request.method == "POST":
        form = LandingPageForm(
            request.POST,
            instance=page,
        )

        if form.is_valid():
            form.save()

            return redirect(
                "landing-page-manage",
                page_id=page.id,
            )
    else:
        form = LandingPageForm(
            instance=page,
        )

    return render(
        request,
        "accounts/landing_page_manage.html",
        {
            "page": page,
            "profile": page.profile,
            "form": form,
        },
    )