from django import forms
from outflow import models


class OutflowForm(forms.ModelForm):

    class Meta:
        model = models.Outflow
        fields = ["product", "quantity", "description"]
        widgets = {
            "product": forms.Select(attrs={"class": "form-control"}),
            "quantity": forms.NumberInput(attrs={"class": "form-control", "min": "1"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }

        labels = {
            "product": "Produto",
            "quantity": "Quantidade",
            "description": "Descrição",
        }

    def clean_quantity(self):
        quantity = self.cleaned_data.get("quantity")
        product = self.cleaned_data.get("product")

        if quantity and product.quantity:
            if quantity > product.quantity:
                raise forms.ValidationError(
                    f"a quantidade disponível em estoque para {product.name} é {product.quantity} unidades."
                )
        return quantity
