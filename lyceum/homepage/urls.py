from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="homepage view"),
    path("coffee/", views.coffee_status, name="coffe roflan"),
]
