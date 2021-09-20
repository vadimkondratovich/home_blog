from django.urls import path
from project.views import projects

urlpatterns = [
    path("", projects, name="project"),
]
