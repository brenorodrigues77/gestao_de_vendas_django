from django.urls import path
from . import views

urlpatterns = [
    path("inflow/list", views.BrandListView.as_view(), name="inflow_list"),
    path("inflow/create", views.BrandCreateView.as_view(), name="inflow_create"),
    path("inflow/<int:pk>/detail",
         views.BrandDetailView.as_view(), name="inflow_detail"),
]
