from django.shortcuts import render

def dashboard_home(request):
    product_metrics = {
        "total_products": 100,
        "stock_cost": 500,
        "total_profit": 700,
        "stock_value": 200
    }
    
    context = {
        "product_metrics": product_metrics
    }
    return render(request, "dashboard.html", context)