from rest_framework import serializers

from products.models import Product, Category, File


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title', 'avatar', 'description']


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['title', 'file']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)
    files = FileSerializer(many=True)

    class Meta:
        model = Product
        fields = ['title', 'description', 'avatar', 'category', 'files']
