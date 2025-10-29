from django.shortcuts import render

def dashboard_home(request):
    context = {}
    return render(request, "dashboard.html", context)