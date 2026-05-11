from django.urls import path

from . import views

app_name = "progress"

urlpatterns = [
    path("", views.journey, name="journey"),
    path("milestones/", views.milestone_list, name="milestones"),
    path("<slug:slug>/", views.topic_detail, name="topic_detail"),
]
