from django.urls import path
from services.views import service_page

urlpatterns = [
    path("", service_page, name="service_page"),
]
