from django.http import HttpResponse
import django.shortcuts
from django.urls import path


def item_list(request):
    template = "catalog/catalog.html"
    blocks = [
        "Колбаса",
        "Йогурт",
        "Мясо",
        "Хлеб",
        "Вода",
        "Колбаса",
        "Йогурт",
        "Мясо",
        "Хлеб",
        "Вода",
    ]
    context = {"carousel_items": blocks}
    return django.shortcuts.render(request, template, context)


def item_detail(request, pk):
    return HttpResponse(f"<body>Подробно элемент {pk}</body>")
