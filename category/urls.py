from django.urls import path
from . import views

urlpatterns = [
    path("category/list", views.CategoryListView.as_view(), name="category_list"),
    path("category/create", views.CategoryCreateView.as_view(),
         name="category_create"),
    path("category/<int:pk>/detail",
         views.CategoryDetailView.as_view(), name="category_detail"),
]
