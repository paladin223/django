from django.urls import path

from . import views

urlpatterns = [
    path("", views.home),
    path("coffee/", views.permission_denied_coffee),
]
