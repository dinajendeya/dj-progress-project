from django.db import models


class SiteProfile(models.Model):
    """Singleton-style site-wide profile content for Dina."""

    owner_name = models.CharField(max_length=120, default="Dina Jendeya")
    tagline = models.CharField(
        max_length=200,
        default="Cybersecurity learner. Mentee. Builder in progress.",
    )
    short_bio = models.TextField(blank=True)
    about_body = models.TextField(blank=True)
    mentorship_blurb = models.TextField(blank=True)
    contact_email = models.EmailField(blank=True)
    linkedin_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    location = models.CharField(max_length=120, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Site profile"
        verbose_name_plural = "Site profile"

    def __str__(self) -> str:
        return f"Site profile ({self.owner_name})"

    @classmethod
    def get_solo(cls) -> "SiteProfile":
        obj = cls.objects.first()
        if obj is None:
            obj = cls.objects.create()
        return obj
