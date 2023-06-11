from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from shop_api import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('product.urls')),
    path('api/v1/users/', include('users.urls')),
    path('api/v1/product/', include('product.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)