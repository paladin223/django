from django.urls import path
from django.urls import re_path
from django.urls import register_converter

from . import converters
from . import views

register_converter(converters.reg_check, "int_val")


urlpatterns = [
    path("", views.item_list),
    path("<int:pk>/", views.item_detail),
    path("converter/<int_val:value>/", views.reg_value),
    re_path(r"^re/(?P<pk>[1-9][0-9]*)/$", views.re_path_value),
]
