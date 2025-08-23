from django.shortcuts import render
from django.views.generic import ListView

from category import models


class CategoryListView(ListView):
    model = models.Category
    template_name = "category_list.html"
    context_object_name = "category"
