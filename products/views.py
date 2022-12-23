from django.shortcuts import render
from .models import Product, ProductCategory


def index(request):
    context = {
        'title': 'Store'
    }
    return render(request, 'products/index.html', context)


def products(request):
    product = Product.objects.all()
    category = ProductCategory.objects.all()
    context = {
        'title': 'Store - Каталог',
        'products': product,
        'categories': category,
    }
    return render(request, 'products/products.html', context)
