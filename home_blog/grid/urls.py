from django.urls import path
from blog.views import blog_grid

urlpatterns = [
    path("", blog_grid, name="blogs_grid"),
]
