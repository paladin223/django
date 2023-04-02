from http import HTTPStatus

from django.db.models.functions import Lower
from django.http import HttpResponse
import django.shortcuts

import catalog.models


def homepage(request):
    template = "homepage/homepage.html"
    context = {
        "items": catalog.models.Item.objects.published()
        .filter(is_on_main=True)
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
        )
        .order_by(Lower("name")),
        "show_category": True,
    }
    return django.shortcuts.render(request, template, context)


def permission_denied_coffee(request):
    return HttpResponse("<body>Я чайник</body>", status=HTTPStatus.IM_A_TEAPOT)
