from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path

urlpatterns = [
    path("", include("homepage.urls"), name="homepage"),
    path("about/", include("about.urls"), name="about"),
    path("catalog/", include("catalog.urls"), name="catalog"),
    path("admin/", admin.site.urls, name="admin"),
    path("feedback/", include("feedback.urls"), name="feedback"),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += (path("__debug__/", include(debug_toolbar.urls)),)
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
