from django.contrib import admin

from .models import SiteProfile


@admin.register(SiteProfile)
class SiteProfileAdmin(admin.ModelAdmin):
    list_display = ("owner_name", "tagline", "updated_at")
    fieldsets = (
        ("Identity", {"fields": ("owner_name", "tagline", "location")}),
        ("Content", {"fields": ("short_bio", "about_body", "mentorship_blurb")}),
        (
            "Contact & Social",
            {"fields": ("contact_email", "linkedin_url", "github_url", "twitter_url")},
        ),
    )

    def has_add_permission(self, request):
        if SiteProfile.objects.exists():
            return False
        return super().has_add_permission(request)
