from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from brands import models, forms


class BrandListView(ListView):
    model = models.Brand
    template_name = "brands_list.html"
    context_object_name = "brands"

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get("name")

        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset


class BrandCreateView(CreateView):
    model = models.Brand
    template_name = "brands_create.html"
    form_class = forms.BrandForm
    success_url = reverse_lazy("brands_list")


class BrandDetailView(DetailView):
    model = models.Brand
    template_name = "brands_detail.html"


class BrandUpdateView(UpdateView):
    model = models.Brand
    form_class = forms.BrandForm
    template_name = "brands_update.html"
    success_url = reverse_lazy("brands_list")


class BrandDeleteView(DeleteView):
    model = models.Brand
    template_name = "brands_delete.html"
    success_url = reverse_lazy("brands_list")
