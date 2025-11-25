from django.utils.formats import number_format
from django.utils import timezone
from django.db.models import Sum, F
from product.models import Product
from outflow.models import Outflow
from category.models import Category
from brands.models import Brand

  
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


def get_sales_value_data():
    today = timezone.now().date()
    dates = [str(today - timezone.timedelta(days=i)) for i in range(6, -1, -1)]
    values = list()

    for date in dates:
        sales_total = Outflow.objects.filter(created_at__date=date).aggregate(
            total_sales=Sum(F('product__selling_price') * F('quantity'))
        )['total_sales'] or 0
        values.append(float(sales_total))

    return dict(dates=dates, values=values)

def get_daily_sales_quantity_data():
    today = timezone.now().date()
    dates = [str(today - timezone.timedelta(days=i)) for i in range(6, -1, -1)]
    quantities = list()

    for date in dates:
        total_quantity = Outflow.objects.filter(created_at__date=date).count()
        quantities.append(total_quantity)

    return dict(dates=dates, values=quantities)


def get_products_by_category_data():
    categories = Category.objects.all()
    return {category.name: Product.objects.filter(category=category).count() for category in categories}

def get_products_by_brand_data():
    brands = Brand.objects.all()
    return {brand.name: Product.objects.filter(brand=brand).count() for brand in brands}