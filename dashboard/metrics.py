from django.utils.formats import number_format
from product.models import Product
  
def get_product_metrics():
    products = Product.objects.all()
    
    total_products = sum(product.quantity * product.cost_price for product in products)
    stock_cost = sum(product.selling_price * product.quantity for product in products)
    total_profit = sum(product.quantity for product in products)
    stock_value = stock_cost - total_profit
    
    return dict(
        total_products=number_format(total_products, decimal_pos=2, force_grouping=True),
        stock_cost=number_format(stock_cost, decimal_pos=2, force_grouping=True),
        total_profit=number_format(total_profit, decimal_pos=2, force_grouping=True),
        stock_value=number_format(stock_value, decimal_pos=2, force_grouping=True)
    )