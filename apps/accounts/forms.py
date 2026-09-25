from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from apps.pages.models import LandingPage


User = get_user_model()


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            "username",
            "password1",
            "password2",
        )


class LandingPageForm(forms.ModelForm):

    class Meta:
        model = LandingPage
        fields = (
            "slug",
            "headline",
            "description",
            "button_text",
            "button_url",
            "template",
            "published",
        )