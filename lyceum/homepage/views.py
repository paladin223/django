from http import HTTPStatus

from django.db.models.functions import Lower
from django.http import HttpResponse
import django.shortcuts

import catalog.models


def homepage(request):
    template = "homepage/homepage.html"
    context = {
        "items": catalog.models.Item.objects.published().order_by(
            Lower("name")
        )
    }
    return django.shortcuts.render(request, template, context)


def permission_denied_coffee(request):
    return HttpResponse("<body>Я чайник</body>", status=HTTPStatus.IM_A_TEAPOT)
