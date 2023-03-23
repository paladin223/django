import django.shortcuts
from django.urls import path


def homepage(request):
    template = "index.html"
    context = {}
    return django.shortcuts.render(request, template, context)
