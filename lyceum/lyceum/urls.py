from django.conf import settings
from django.contrib import admin
from django.urls import include
from django.urls import path

urlpatterns = [
    path("about/", include("about.urls")),
    path("admin/", admin.site.urls),
    path("catalog/", include("catalog.urls")),
    path("homepage/", include("homepage.urls")),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += (path("__debug__/", include(debug_toolbar.urls)),)
