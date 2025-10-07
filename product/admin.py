from django.contrib import admin

from brands import models
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'category', 'cost_price',
                    'selling_price', 'quantity', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    list_filter = ('brand', 'category')


admin.site.site_header = "Administração de Produtos"
admin.site.register(Product, ProductAdmin)
