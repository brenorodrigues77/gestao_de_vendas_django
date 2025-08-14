from django.urls import path
from . import views

urlpatterns = [
    path("brand/list", views.BrandListView.as_view(), name="brand_list"),
]
