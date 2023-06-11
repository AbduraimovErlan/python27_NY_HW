from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from shop_api import settings
from product.views import (
    category_list_create_api_view,
    category_retrieve_update_delete_api_view,
    product_list_create_api_view,
    product_retrieve_update_delete_api_view,
    review_list_create_api_view,
    review_retrieve_update_delete_api_view,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/categories/', category_list_create_api_view),
    path('api/v1/categories/<int:id>/', category_retrieve_update_delete_api_view),
    path('api/v1/products/', product_list_create_api_view),
    path('api/v1/products/<int:id>/', product_retrieve_update_delete_api_view),
    path('api/v1/reviews/', review_list_create_api_view),
    path('api/v1/reviews/<int:id>/', review_retrieve_update_delete_api_view),
    path('api/v1/users/', include('users.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)