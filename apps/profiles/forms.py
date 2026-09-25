from django import forms

from .models import SocialProfile


class SocialProfileForm(forms.ModelForm):
    class Meta:
        model = SocialProfile
        fields = [
            "platform",
            "profile_url",
            "username",
            "display_name",
            "bio",
            "profile_image",
        ]

        widgets = {
            "platform": forms.Select(),
            "profile_url": forms.URLInput(
                attrs={
                    "placeholder": "https://www.tiktok.com/@username",
                }
            ),
            "username": forms.TextInput(
                attrs={
                    "placeholder": "username",
                }
            ),
            "display_name": forms.TextInput(
                attrs={
                    "placeholder": "Your display name",
                }
            ),
            "bio": forms.Textarea(
                attrs={
                    "placeholder": "Tell people about yourself...",
                    "rows": 4,
                }
            ),
            "profile_image": forms.ClearableFileInput(),
        }