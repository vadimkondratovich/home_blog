from django.urls import path
from grid.views import blog_grid

urlpatterns = [
    path("", blog_grid, name="blog_grid"),
]
