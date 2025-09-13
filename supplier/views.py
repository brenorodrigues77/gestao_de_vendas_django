from django.shortcuts import render
from supplier import models
from django.views.generic import ListView


class SupplierListView(ListView):
    model = models.Supplier
    template_name = "supplier_list.html"
    context_object_name = "supplier"
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get("name")

        if name:
            queryset = queryset.filter(name__icontains=name)
            if not queryset.exists():
                self.extra_context = {"not_found": "Fornecedor nao encontrado"}

        return queryset
