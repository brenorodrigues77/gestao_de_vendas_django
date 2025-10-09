from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from product import models, forms


class ProductListView(ListView):
    model = models.Product
    template_name = "product_list.html"
    context_object_name = "product"
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get("name")

        if name:
            queryset = queryset.filter(name__icontains=name)
            if not queryset.exists():
                self.extra_context = {"not_found": "Produto não encontrado"}

        return queryset


class ProductCreateView(CreateView):
    model = models.Product
    template_name = "product_create.html"
    form_class = forms.ProductForm
    success_url = reverse_lazy("product_list")


class ProductDetailView(DetailView):
    model = models.Product
    template_name = "product_detail.html"


class ProductUpdateView(UpdateView):
    model = models.Product
    form_class = forms.ProductForm
    template_name = "product_update.html"
    success_url = reverse_lazy("product_list")


class ProductDeleteView(DeleteView):
    model = models.Product
    template_name = "product_delete.html"
    success_url = reverse_lazy("product_list")
