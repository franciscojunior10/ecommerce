from django.shortcuts import render

# Create your views here.

from .models import Product, Category

def productList(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'catalog/product_list.html', context)

def category(request, slug):
    category = Category.objects.get(slug=slug)
    context = {
        'current_category': category,
        'products': Product.objects.filter(category=category), 
    }
    return render(request, 'catalog/category.html', context)