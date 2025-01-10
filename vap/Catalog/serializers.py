from .models import Product, Category
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug', 'description', 'is_active', 'meta_keywords', 'meta_description')



class ProductSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)
    
    class Meta:
        model = Product
        fields = ('name', 'slug', 'sku', 'base_price', 'image', 'lot_size', 'is_active', 'is_featured', 'current_stock', 'description', 'meta_keywords', 'categories')