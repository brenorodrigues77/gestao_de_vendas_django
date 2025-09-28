from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from inflow import forms
from .models import Inflow


class InflowListView(ListView):
    model = Inflow
    template_name = "inflow_list.html"
    context_object_name = "inflows"
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        product = self.request.GET.get("product")

        if product:
            queryset = queryset.filter(product__name__icontains=product)
            if not queryset.exists():
                self.extra_context = {"not_found": "Entrada não encontrada"}

        return queryset


class InflowCreateView(CreateView):
    model = Inflow
    template_name = "inflow_create.html"
    form_class = forms.InflowForm
    success_url = reverse_lazy("inflow_list")


class InflowDetailView(DetailView):
    model = Inflow
    template_name = "inflow_detail.html"
    context_object_name = "inflow"
