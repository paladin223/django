import django.db.models
from django.http import HttpResponse
import django.shortcuts
from django.shortcuts import get_object_or_404

import catalog.models


def item_list(request):
    template = "catalog/catalog.html"
    context = {
        "items": catalog.models.Item.objects.published().order_by(
            "name", "category"
        ),
        "show_category": False,
    }

    return django.shortcuts.render(request, template, context)


def item_detail(request, pk):
    template = "catalog/includes/item.html"
    item = get_object_or_404(
        catalog.models.Item.objects.published(),
        id=pk,
    )
    context = {"item": item}
    return django.shortcuts.render(request, template, context)


def item_detail_old(request, pk):
    return HttpResponse(f"<body>Подробно элемент {pk}</body>")
