from django.contrib import admin
from django.urls import include, path
from wagtail import urls as wagtail_urls

urlpatterns = [
    path("django-admin/", admin.site.urls),
    path("admin/", include("wagtail.admin.urls")),
    path("documents/", include("wagtail.documents.urls")),
    path("", include(wagtail_urls)),
]
