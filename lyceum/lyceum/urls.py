from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path

urlpatterns = [
    path("", include("homepage.urls"), name="main_page"),
    path("about/", include("about.urls"), name="aboгte"),
    path("catalog/", include("catalog.urls"), name="catalog"),
    path("admin/", admin.site.urls, name="admin"),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += (path("__debug__/", include(debug_toolbar.urls)),)
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
