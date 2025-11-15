from django.utils.formats import number_format
from django.db.models import Sum
from product.models import Product
from outflow.models import Outflow
  
def get_product_metrics():
    products = Product.objects.all()
    
    total_products = products.count()
    
    stock_cost = sum(product.cost_price * product.quantity for product in products)
    stock_value = sum(product.selling_price * product.quantity for product in products)
    total_profit = stock_value - stock_cost
    total_quantity = sum(product.quantity for product in products)
    
    return dict(
        total_products=number_format(total_products, decimal_pos=0, force_grouping=True),
        stock_cost=number_format(stock_cost, decimal_pos=2, force_grouping=True),
        total_profit=number_format(total_profit, decimal_pos=2, force_grouping=True),
        stock_value=number_format(stock_value, decimal_pos=2, force_grouping=True),
        total_quantity=total_quantity
    )

def get_sales_metrics():

    total_sales = Outflow.objects.count()
    total_products_sold = Outflow.objects.aggregate(total_quantity_sold=Sum('quantity'))['total_quantity_sold'] or 0
    total_sales_value = sum(outflow.quantity * outflow.product.selling_price for outflow in Outflow.objects.all())
    total_sales_profit = sum(outflow.quantity * (outflow.product.selling_price - outflow.product.cost_price) for outflow in Outflow.objects.all())

    return dict(
       products_sold=total_products_sold,
       total_sales_value=total_sales_value,
       total_sales=total_sales,
       total_sales_profit=total_sales_profit
    )