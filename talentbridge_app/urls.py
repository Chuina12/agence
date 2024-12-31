from django.urls import path
from .import views


urlpatterns=[
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("team_details", views.team_details, name="team_details"),
    path("jobs", views.jobs, name="jobs"),
    path("services", views.services, name="services"),
    path("history", views.history, name="history"),
    path('contact', views.contact, name="contact"),
    path('faq', views.faq, name="faq"),
    path('project', views.project, name="project"),
    path('blog', views.blog, name="blog"),
    path('blog_details', views.blog_details, name="blog_details"),
    path('project_details', views.project_details, name="project_details"),

]