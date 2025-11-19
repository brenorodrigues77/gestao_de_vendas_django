import json
from django.shortcuts import render
from dashboard import metrics

def dashboard_home(request):
    product_metrics = metrics.get_product_metrics()
    sales_metrics = metrics.get_sales_metrics()
    sales_value_data = metrics.get_sales_value_data()

    context = {
        "product_metrics": product_metrics,
        "sales_metrics": sales_metrics,
        "sales_value_data": json.dumps(sales_value_data)
    }
    return render(request, "dashboard.html", context)