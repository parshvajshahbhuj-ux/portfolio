from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("portfolio.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Custom admin branding
admin.site.site_header = "Parshva Shah — Portfolio Admin"
admin.site.site_title = "Portfolio Admin"
admin.site.index_title = "Dashboard"
