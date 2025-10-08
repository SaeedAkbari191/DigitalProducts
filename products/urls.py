from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import ProductListView, ProductDetailView, CategoryListView, CategoryDetailView, FileDetailView, \
    FileListView

# router = DefaultRouter()
# router.register('products', ProductListView)

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),

    path('products/<int:product_pk>/files/', FileListView.as_view(), name='file-list'),
    path('products/<int:product_pk>/files/<int:pk>/', FileDetailView.as_view(), name='file-detail'),

    path('category/', CategoryListView.as_view(), name='category-list'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),

]
