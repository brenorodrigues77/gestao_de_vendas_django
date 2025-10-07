from django.contrib import admin
from outflow import models


class OutflowAdmin(admin.ModelAdmin):
    list_display = ('product',)
    search_fields = ('product__name', 'description',)


admin.site.site_header = "Administração de Saída de Vendas"
admin.site.register(models.Outflow, OutflowAdmin)
