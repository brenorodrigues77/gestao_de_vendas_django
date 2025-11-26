from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("", include("dashboard.urls")),
    path("", include("brands.urls")),
    path("", include("category.urls")),
    path("", include("supplier.urls")),
    path("", include("product.urls")),
    path("", include("inflow.urls")),
    path("", include("outflow.urls")),
]
