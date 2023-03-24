from django.http import HttpResponse
import django.shortcuts
from django.urls import path


def item_list(request):
    template = "catalog/main.html"
    context = {}
    return django.shortcuts.render(request, template, context)


def item_detail(request, pk):
    return HttpResponse(f"<body>Подробно элемент {pk}</body>")
