from django import forms

from apps.pages.models import LandingPage


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