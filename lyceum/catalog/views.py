import django.db.models
from django.http import HttpResponse
import django.shortcuts
from django.shortcuts import get_object_or_404

import catalog.models


def item_list(request):
    template = "catalog/catalog.html"
    context = {
        "items": catalog.models.Item.objects.published()
        .only(
            catalog.models.Item.name.field.name,
            catalog.models.Item.text.field.name,
            catalog.models.Item.tags.field.name,
        )
        .order_by("category"),
        "show_category": False,
    }

    return django.shortcuts.render(request, template, context)


def item_detail(request, pk):
    template = "catalog/includes/item.html"
    item = get_object_or_404(
        catalog.models.Item.objects.published()
        .select_related(
            catalog.models.Category._meta.model_name,
            "mainimage",
        )
        .only(
            catalog.models.Item.name.field.name,
            catalog.models.Item.text.field.name,
            f"{catalog.models.Item.category.field.name}"
            f"__{catalog.models.Category.name.field.name}",
            catalog.models.Item.tags.field.name,
        ),
        id=pk,
    )
    context = {"item": item}
    return django.shortcuts.render(request, template, context)


def item_detail_old(request, pk):
    return HttpResponse(f"<body>Подробно элемент {pk}</body>")
