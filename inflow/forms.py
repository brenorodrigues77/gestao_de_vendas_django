from django import forms
from inflow import models


class InflowForm(forms.ModelForm):
    class Meta:
        model = models.Inflow
        fields = ["product", "supplier", "quantity", "description"]
        widgets = {
            "product": forms.Select(attrs={"class": "form-control"}),
            "supplier": forms.Select(attrs={"class": "form-control"}),
            "quantity": forms.NumberInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
        }
        labels = {
            "product": "Produto",
            "supplier": "Fornecedor",
            "quantity": "Quantidade",
            "description": "Descrição",
        }
        help_texts = {
            "product": "Selecione o produto que está entrando no estoque.",
            "supplier": "Selecione o fornecedor do produto.",
            "quantity": "Informe a quantidade do produto.",
            "description": "Adicione uma descrição para o produto.",
        }
