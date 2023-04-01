from django.http import HttpResponse
import django.shortcuts
import django.db.models

import catalog.models


def item_list(request):
    template = "catalog/catalog.html"
    context = {"items": catalog.models.Item.objects.published()
               .order_by("category")}

    return django.shortcuts.render(request, template, context)


def item_detail(request, pk):
    return HttpResponse(f"<body>Подробно элемент {pk}</body>")
