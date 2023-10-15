from django.contrib import admin
from django.urls import path, include 
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # App URL's
    path("", include("website.urls", namespace="website")),
    path("store/", include("store.urls", namespace="store"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
