from django.shortcuts import render
from rest_framework import viewsets

from products.models import Product
from products.serializers import ProductSerializer


# Create your views here.

class ProductListView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
