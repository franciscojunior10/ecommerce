from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.

class Index(TemplateView):
    template_name = 'index.html'

class Contact(TemplateView):
    template_name = 'contact.html'

class ProductList(TemplateView):
    template_name = 'product_list.html'

class Product(TemplateView):
    template_name = 'product.html'