from django.contrib import admin
from category import models


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description',)
    search_fields = ('name', 'description',)


admin.site.site_header = "Administração de Categorias"
admin.site.register(models.Category, CategoryAdmin)
