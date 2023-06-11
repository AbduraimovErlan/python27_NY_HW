from . import views
from django.urls import path





urlpatterns =[
    path('categories/', views.CategoryListAPIView.as_view()),
    path('categories/<int:id>/', views.CategoryDetailAPIView.as_view()),
    path('reviews/', views.ReviewAPIViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('reviews/<int:id>/', views.ReviewAPIViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}
    )),
    path('products/', views.ProductListCreateAPIView.as_view()),
    path('products/<int:id>/', views.CategoryDetailAPIView.as_view()),
]