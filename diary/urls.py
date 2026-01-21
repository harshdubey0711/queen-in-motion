from django.urls import path
from . import views
from .views import create_superuser_once

urlpatterns = [
    path('', views.diary_view, name='home'),
    path("create-superuser/", create_superuser_once),

]