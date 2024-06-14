
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("djoser.urls")),
    path("api/", include("api.urls")),
    path("api/products/", include("product.urls")),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
