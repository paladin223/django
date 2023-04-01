from django.urls import path
from django.urls import re_path
from django.urls import register_converter

from . import converters
from . import views

register_converter(converters.RegCheck, "int_val")

app_name = "catalog"

urlpatterns = [
    path("", views.item_list, name="main"),
    path("<int:pk>/", views.item_detail, name="item_detail"),
    path(
        "converter/<int_val:pk>/", views.item_detail_old,
        name="catalog_converter"
    ),
    re_path(
        r"^re/(?P<pk>[1-9][0-9]*)/$",
        views.item_detail_old,
        name="catalog re_path",
    ),
]
