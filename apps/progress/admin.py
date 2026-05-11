from django.contrib import admin

from .models import Milestone, ProgressEntry, Topic


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "status",
        "progress_percent",
        "display_order",
        "updated_at",
    )
    list_filter = ("status",)
    search_fields = ("title", "summary", "description")
    prepopulated_fields = {"slug": ("title",)}
    ordering = ("display_order", "title")


@admin.register(ProgressEntry)
class ProgressEntryAdmin(admin.ModelAdmin):
    list_display = ("title", "topic", "entry_type", "status", "entry_date")
    list_filter = ("status", "entry_type", "topic")
    search_fields = ("title", "summary", "body")
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = "entry_date"
    autocomplete_fields = ("topic",)


@admin.register(Milestone)
class MilestoneAdmin(admin.ModelAdmin):
    list_display = ("title", "topic", "importance", "achieved_on")
    list_filter = ("importance", "topic")
    search_fields = ("title", "description")
    date_hierarchy = "achieved_on"
    autocomplete_fields = ("topic",)
