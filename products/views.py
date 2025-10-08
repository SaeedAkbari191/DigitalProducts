from itertools import product

from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from products.models import Product, Category, File
from products.serializers import ProductSerializer, CategorySerializer, FileSerializer


# Create your views here.
class CategoryListView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True, context={'request': request})
        return Response(serializer.data)


class CategoryDetailView(APIView):
    def get(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializer(category, context={'request': request})
        return Response(serializer.data)


class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True, context={'request': request})
        return Response(serializer.data)


class ProductDetailView(APIView):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product, context={'request': request})
        return Response(serializer.data)


class FileListView(APIView):
    def get(self, request, product_pk):
        files = File.objects.filter(product_id=product_pk)
        serializer = FileSerializer(files, many=True, context={'request': request})
        return Response(serializer.data)


class FileDetailView(APIView):
    def get(self, request, product_pk, pk):
        file = get_object_or_404(File, pk=pk, product_id=product_pk)
        serializer = FileSerializer(file, context={'request': request})
        return Response(serializer.data)

# class ProductListView(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#     def create(self, request, *args, **kwargs):
#         return super().create(request, *args, **kwargs)


# class ProductDetailView(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#
# def retrieve(self, request, *args, **kwargs):
#     product = self.get_object()
#     serializer = self.get_serializer(product)
#     return Response(serializer.data)
