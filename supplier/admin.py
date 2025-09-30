from django.contrib import admin
from inflow import models


class SupplierAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description',)
    search_fields = ('name', 'description',)


admin.site.site_header = "Administração de Fornecedores"
admin.site.register(models.Supplier, SupplierAdmin)
