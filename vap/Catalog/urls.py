from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product/<slug:slug>/', views.product, name='product'),
    path('products/<str:category>', views.productsByCategory, name='productsByCategory'),
    path('search/', views.search, name='search'),
    path('api/products/', views.api_products, name='api_products'),
    path('api/product/<int:product_id>/', views.api_product, name='api_product'),
]