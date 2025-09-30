from django.contrib import admin
from inflow import models


class InflowAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'quantity',
                    'supplier', 'created_at', 'description')
    search_fields = ('product__name', 'supplier__name', 'description')


admin.site.site_header = "Administração de Entradas"
admin.site.register(models.Inflow, InflowAdmin)
