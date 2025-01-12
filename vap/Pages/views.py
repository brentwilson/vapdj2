from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    context = {}
    context['page_title'] = 'Home'
    
    return render(request, 'index.html', context)

def page(request, slug):
    context = {}
    context['page_title'] = slug
    page = Page.objects.get(slug=slug)
    context['page'] = page
    
    return render(request, 'page.html', context)