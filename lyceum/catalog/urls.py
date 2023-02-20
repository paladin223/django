from django.urls import path
from django.urls import re_path
from django.urls import register_converter

from . import converters
from . import views

register_converter(converters.reg_check, "int_val")


urlpatterns = [
    path("", views.item_list, name="main ctalog page"),
    path("<int:pk>/", views.item_detail, name="catalog detalisation"),
    path(
        "converter/<int_val:pk>/", views.item_detail, name="catalog converter"
    ),
    re_path(
        r"^re/(?P<pk>[1-9][0-9]*)/$",
        views.item_detail,
        name="catalog re_path",
    ),
]
