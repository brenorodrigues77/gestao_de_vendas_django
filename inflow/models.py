from django.db import models
from product.models import Product
from supplier.models import Supplier


class Inflow(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, related_name="product"
    )
    supplier = models.ForeignKey(
        Supplier, on_delete=models.PROTECT, related_name="supplier")
    quantity = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return str(self.product)
