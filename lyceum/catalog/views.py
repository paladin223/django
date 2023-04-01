import django.db.models
import django.shortcuts
from django.shortcuts import get_object_or_404

import catalog.models


def item_list(request):
    template = "catalog/catalog.html"
    context = {
        "items": catalog.models.Item.objects.published().order_by("category")
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
