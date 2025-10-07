from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from .models import Outflow
from outflow import forms


class OutflowListView(ListView):
    model = Outflow
    template_name = "outflow_list.html"
    context_object_name = "outflows"
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        product = self.request.GET.get("product")

        if product:
            queryset = queryset.filter(product__name__icontains=product)
            if not queryset.exists():
                self.extra_context = {"not_found": "Saída não encontrada"}

        return queryset


class OutflowCreateView(CreateView):
    models = Outflow
    template_name = "outflow_create.html"
    form_class = forms.OutflowForm
    success_url = reverse_lazy("outflow_list")


class OutflowDetailView(DetailView):
    model = Outflow
    template_name = "outflow_detail.html"
    context_object_name = "outflow"
