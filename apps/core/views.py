from django.shortcuts import render

from apps.blog.models import Post
from apps.progress.models import Milestone, ProgressEntry, Topic


def home(request):
    topics = list(Topic.objects.all()[:6])
    recent_entries = list(
        ProgressEntry.objects.filter(
            status=ProgressEntry.Status.PUBLISHED
        ).select_related("topic")[:4]
    )
    recent_milestones = list(Milestone.objects.select_related("topic").all()[:4])
    featured_posts = list(
        Post.objects.filter(status=Post.Status.PUBLISHED, featured=True)[:2]
    )
    return render(
        request,
        "core/home.html",
        {
            "topics": topics,
            "recent_entries": recent_entries,
            "recent_milestones": recent_milestones,
            "featured_posts": featured_posts,
        },
    )


def about(request):
    return render(request, "core/about.html")


def contact(request):
    return render(request, "core/contact.html")
