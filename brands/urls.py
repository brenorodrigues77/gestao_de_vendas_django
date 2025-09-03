from django.urls import path
from . import views

urlpatterns = [
    path("brands/list", views.BrandListView.as_view(), name="brands_list"),
    path("brands/create", views.BrandCreateView.as_view(), name="brands_create"),
    path("brands/<int:pk>/detail",
         views.BrandDetailView.as_view(), name="brands_detail"),
]
