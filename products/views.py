from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView
from products.models import Product

class ProductListView(ListView):
	template_name = "products/product_list.html"
	model = Product

	def get_queryset(self):
		qs = super(ProductListView, self).get_queryset()
		qs = [qs[0]] * 8
		return qs

class ProductDetailView(DetailView):
	template_name = "products/product.html"
	model = Product
