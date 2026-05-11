"""Seed initial topics, sample entries, and a starter blog post."""

from datetime import date, timedelta

from django.core.management.base import BaseCommand

from apps.blog.models import Post
from apps.core.models import SiteProfile
from apps.progress.models import Milestone, ProgressEntry, Topic

TOPICS = [
    {
        "title": "Linux Journey",
        "summary": "Comfort in the terminal: filesystem, permissions, processes, shell.",
        "icon": "$_",
        "status": Topic.Status.ACTIVE,
        "progress_percent": 55,
        "display_order": 10,
    },
    {
        "title": "CCNA Networking",
        "summary": "Networking fundamentals: OSI, IP, subnetting, routing, switching.",
        "icon": "::",
        "status": Topic.Status.ACTIVE,
        "progress_percent": 35,
        "display_order": 20,
    },
    {
        "title": "Programming with Python",
        "summary": "From scripts to small tools: syntax, data structures, automation.",
        "icon": ">>>",
        "status": Topic.Status.ACTIVE,
        "progress_percent": 50,
        "display_order": 30,
    },
    {
        "title": "OverTheWire Bandit",
        "summary": "Wargame to build practical Linux + recon muscle memory.",
        "icon": "<>",
        "status": Topic.Status.ACTIVE,
        "progress_percent": 40,
        "display_order": 40,
    },
    {
        "title": "TryHackMe Security 101",
        "summary": "Hands-on intro to cybersecurity: tools, attacks, defenses.",
        "icon": "#!",
        "status": Topic.Status.ACTIVE,
        "progress_percent": 30,
        "display_order": 50,
    },
    {
        "title": "Building This Blog",
        "summary": "Designing and shipping this Django site to share the journey.",
        "icon": "{}",
        "status": Topic.Status.ACTIVE,
        "progress_percent": 70,
        "display_order": 60,
    },
]


class Command(BaseCommand):
    help = "Seed the database with starter topics, entries, milestones, and a post."

    def handle(self, *args, **options):
        # Site profile
        profile = SiteProfile.get_solo()
        if not profile.short_bio:
            profile.short_bio = (
                "I'm learning cybersecurity in public — building skills across "
                "Linux, networking, Python, and offensive security through mentorship."
            )
        if not profile.mentorship_blurb:
            profile.mentorship_blurb = (
                "Cybersecurity is not just an IT-expert topic. With mentorship, "
                "I've been working through Linux Journey, CCNA networking, "
                "programming with Python, OverTheWire Bandit, TryHackMe Security 101, "
                "and building this blog — one focused step at a time."
            )
        profile.save()
        self.stdout.write(self.style.SUCCESS("Site profile ensured."))

        # Topics
        topic_objs = {}
        for data in TOPICS:
            obj, created = Topic.objects.get_or_create(
                title=data["title"], defaults=data
            )
            topic_objs[data["title"]] = obj
            self.stdout.write(
                ("Created " if created else "Exists  ") + f"topic: {obj.title}"
            )

        today = date.today()

        # Sample progress entries
        sample_entries = [
            (
                "Linux Journey",
                "Filesystem hierarchy clicked",
                "lesson",
                "Walked through /etc, /var, /home and finally got a mental map of where things live.",
            ),
            (
                "OverTheWire Bandit",
                "Cleared the first wave of Bandit levels",
                "win",
                "Used ssh, find, and base tools without constantly reaching for cheatsheets.",
            ),
            (
                "Programming with Python",
                "Wrote a small log parser",
                "update",
                "Practiced file IO, dictionaries, and a tiny CLI.",
            ),
            (
                "CCNA Networking",
                "Subnetting drills",
                "challenge",
                "Drilled VLSM until it felt boring — which is the point.",
            ),
        ]
        for i, (topic_title, title, etype, summary) in enumerate(sample_entries):
            topic = topic_objs[topic_title]
            ProgressEntry.objects.get_or_create(
                topic=topic,
                title=title,
                defaults={
                    "summary": summary,
                    "body": summary,
                    "entry_type": etype,
                    "status": ProgressEntry.Status.PUBLISHED,
                    "entry_date": today - timedelta(days=i * 3),
                },
            )

        # Sample milestones
        sample_milestones = [
            ("OverTheWire Bandit", "Reached Bandit level 10", "major"),
            (
                "Programming with Python",
                "First working script in production-ish use",
                "minor",
            ),
            ("Building This Blog", "Site v1 deployed", "major"),
        ]
        for i, (topic_title, title, importance) in enumerate(sample_milestones):
            topic = topic_objs[topic_title]
            Milestone.objects.get_or_create(
                topic=topic,
                title=title,
                defaults={
                    "achieved_on": today - timedelta(days=i * 5),
                    "importance": importance,
                    "description": "",
                },
            )

        # Starter blog post
        Post.objects.get_or_create(
            title="Why I'm learning cybersecurity in public",
            defaults={
                "excerpt": "Mentorship, momentum, and why I decided to share the journey.",
                "body": (
                    "Cybersecurity is not just an IT-expert topic. "
                    "With my mentor's guidance, I've been working through Linux, "
                    "networking, Python, Bandit, and TryHackMe Security 101 — and "
                    "building this site as part of that journey.\n\n"
                    "This blog is where I'll capture lessons, wins, and the messy "
                    "middle of learning."
                ),
                "status": Post.Status.PUBLISHED,
                "featured": True,
                "published_on": today,
            },
        )

        self.stdout.write(self.style.SUCCESS("Seed complete."))
