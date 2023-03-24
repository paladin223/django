import django.shortcuts
from django.urls import path


def description(request):
    template = "about/main.html"
    context = {}
    return django.shortcuts.render(request, template, context)
