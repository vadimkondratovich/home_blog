from django.urls import path
from blog.views import blog_detail

urlpatterns = [
    path("", blog_detail, name="blog_detail"),
]
