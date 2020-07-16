from django.shortcuts import render
from django.views import generic
from .models import Shop

class HomeView(generic.ListView):
    model = Shop
    context_object_name = 'shops'
    template_name = 'shops/index.html'

class ShopDetailView(generic.DetailView):
    model = Shop
    context_object_name = 'shop'
    template_name = 'shops/shop_detail.html'
