from django.shortcuts import render
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *

# Create your views here.
def index(request):
    context = { 'title': 'Catalog' }
    products = Product.objects.all()
    context['products'] = products
    return render(request, 'index.html', context)

def product(request, slug):
    context = { 'title': slug }
    product = Product.objects.get(slug=slug)
    context['product'] = product
    return render(request, 'product.html', context)

def productsByCategory(request, category):
    context = { 'title': request.GET['category'] }
    products = Product.objects.filter(category__name=category)
    context['products'] = products
    return render(request, 'products_by_category.html', context)

def search(request):
    context = { 'title': 'Search' }
    if request.method == 'POST':
        search_term = request.POST['search_term']
        products = Product.objects.filter(name__icontains=search_term)
        context['products'] = products
    return render(request, 'search.html', context)

@api_view(['GET'])
def api_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def api_product(request, product_id):
    product = Product.objects.get(id=product_id)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)
