from django.shortcuts import get_object_or_404, render

from .models import Milestone, ProgressEntry, Topic


def journey(request):
    topics = Topic.objects.all()
    return render(request, "progress/journey.html", {"topics": topics})


def topic_detail(request, slug):
    topic = get_object_or_404(Topic, slug=slug)
    entries = topic.entries.filter(status=ProgressEntry.Status.PUBLISHED)
    milestones = topic.milestones.all()
    return render(
        request,
        "progress/topic_detail.html",
        {"topic": topic, "entries": entries, "milestones": milestones},
    )


def milestone_list(request):
    milestones = Milestone.objects.select_related("topic").all()
    return render(
        request,
        "progress/milestone_list.html",
        {"milestones": milestones},
    )
