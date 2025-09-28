from django import forms
from inflow import models


class InflowForm(forms.ModelForm):
    class Meta:
        model = models.Inflow
        fields = ["product", "supplier", "quantity", "description"]
        widgets = {
            "product": forms.Select(attrs={"class": "form-control"}),
            "supplier": forms.Select(attrs={"class": "form-control"}),
            "quantity": forms.NumberInput(attrs={"class": "form-control", "min": "1"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }
        labels = {
            "product": "Produto",
            "supplier": "Fornecedor",
            "quantity": "Quantidade",
            "description": "Descrição",
        }

        def clean_quantity(self):
            quantity = self.cleaned_data.get("quantity")
            if quantity is not None and quantity <= 1:
                raise forms.ValidationError(
                    "A quantidade deve ser no mínimo um.")
            return quantity
