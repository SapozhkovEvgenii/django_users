from django.contrib import admin
from django.urls import path, include
from django.conf import settings
# if settings.DEBUG:
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("user.urls")),
    path('posts/', include("post.urls")),
] 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

