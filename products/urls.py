from rest_framework.routers import DefaultRouter
from django.urls import path,include

from .views import ProductListView

router = DefaultRouter()
router.register('products', ProductListView)

urlpatterns = [
    path('', include(router.urls)),
]
