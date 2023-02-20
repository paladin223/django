from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="homepage view"),
    path("coffee/", views.permission_denied_coffee, name="coffe roflan"),
]
