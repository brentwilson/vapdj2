from django.contrib import admin
from .models import Product, Category
from unfold.admin import ModelAdmin
# Register your models here.

@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ['name', 'slug', 'is_active', 'created_at']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ['smallThumbnail','name', 'sku', 'base_price', 'is_active']
    prepopulated_fields = {'slug': ('name',)}
