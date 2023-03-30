from http import HTTPStatus

from django.http import HttpResponse
import django.shortcuts


def homepage(request):
    template = "homepage/homepage.html"
    context = {}
    return django.shortcuts.render(request, template, context)


def permission_denied_coffee(request):
    return HttpResponse("<body>Я чайник</body>", status=HTTPStatus.IM_A_TEAPOT)
