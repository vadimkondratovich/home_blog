from django.urls import path
from projects.views import project_page

urlpatterns = [
    path("", project_page, name="project_page"),
]
