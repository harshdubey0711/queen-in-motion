from django.urls import path
from .views import diary_view, create_superuser_once

urlpatterns = [
    path("", diary_view, name="home"),
    # path("create-superuser/", create_superuser_once),
]
