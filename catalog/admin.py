from django.contrib import admin

# Register your models here.
from .models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created', 'modified']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'created', 'modified']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)