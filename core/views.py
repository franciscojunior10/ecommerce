from django.shortcuts import render
from django.http import HttpResponse

from catalog.models import Category
# from django.views.generic import TemplateView

# Create your views here.

# class Index(TemplateView):
#     template_name = 'index.html'

# class Contact(TemplateView):
#     template_name = 'contact.html'

# class ProductList(TemplateView):
#     template_name = 'product_list.html'

# class Product(TemplateView):
#     template_name = 'product.html'

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def productList(request):
    return render(request, 'product_list.html')

def product(request):
    return render(request, 'product.html')