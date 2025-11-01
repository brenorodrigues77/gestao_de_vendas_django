from django.shortcuts import render
from dashboard import metrics

def dashboard_home(request):
    product_metrics = metrics.get_product_metrics()

    context = {
        "product_metrics": product_metrics
    }
    return render(request, "dashboard.html", context)