from django.contrib import admin

from brands import models
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'serie_number',)
    search_fields = ('name', 'description',)
    list_filter = ('brand', 'category', 'serie_number',)


admin.site.site_header = "Administração de Produtos"
admin.site.register(Product, ProductAdmin)
