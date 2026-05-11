from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Topic(models.Model):
    class Status(models.TextChoices):
        PLANNED = "planned", "Planned"
        ACTIVE = "active", "Active"
        PAUSED = "paused", "Paused"
        COMPLETED = "completed", "Completed"

    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=140, unique=True, blank=True)
    summary = models.CharField(max_length=240, blank=True)
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.ACTIVE
    )
    progress_percent = models.PositiveSmallIntegerField(default=0)
    display_order = models.PositiveSmallIntegerField(default=100)
    icon = models.CharField(max_length=40, blank=True)
    started_on = models.DateField(blank=True, null=True)
    completed_on = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["display_order", "title"]

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)[:140]
        super().save(*args, **kwargs)

    def get_absolute_url(self) -> str:
        return reverse("progress:topic_detail", kwargs={"slug": self.slug})


class ProgressEntry(models.Model):
    class Status(models.TextChoices):
        DRAFT = "draft", "Draft"
        PUBLISHED = "published", "Published"

    class EntryType(models.TextChoices):
        UPDATE = "update", "Update"
        LESSON = "lesson", "Lesson learned"
        REFLECTION = "reflection", "Reflection"
        CHALLENGE = "challenge", "Challenge"
        WIN = "win", "Win"

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="entries")
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    summary = models.CharField(max_length=300, blank=True)
    body = models.TextField()
    entry_type = models.CharField(
        max_length=20, choices=EntryType.choices, default=EntryType.UPDATE
    )
    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.DRAFT
    )
    entry_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-entry_date", "-created_at"]
        verbose_name_plural = "Progress entries"

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)[:200] or "entry"
        super().save(*args, **kwargs)


class Milestone(models.Model):
    class Importance(models.TextChoices):
        MINOR = "minor", "Minor"
        MAJOR = "major", "Major"

    topic = models.ForeignKey(
        Topic, on_delete=models.CASCADE, related_name="milestones"
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    achieved_on = models.DateField()
    importance = models.CharField(
        max_length=10, choices=Importance.choices, default=Importance.MINOR
    )
    evidence_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-achieved_on", "-created_at"]

    def __str__(self) -> str:
        return self.title
