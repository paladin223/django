import django.shortcuts
from django.urls import path


def homepage(request):
    template = "homepage/main.html"
    context = {}
    return django.shortcuts.render(request, template, context)
