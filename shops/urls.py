from django.urls import path
from . import views


app_name = 'shops'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('detail/<int:pk>/', views.ShopDetailView.as_view(), name='detail'),
]
