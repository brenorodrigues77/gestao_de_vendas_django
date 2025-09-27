from django.urls import path
from . import views

urlpatterns = [
    path("inflow/list", views.InflowListView.as_view(), name="inflow_list"),
]
