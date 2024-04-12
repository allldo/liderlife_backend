from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('grappelli/', include('grappelli.urls')), # grappelli URLS
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('api/v1/', include('items.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
