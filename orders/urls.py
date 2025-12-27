# orders/urls.py

from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('', views.order_list_view, name='order_list'),
    path('seller/', views.seller_order_list_view, name='seller_order_list'),
    
    # مسیر جدید برای صفحه نهایی کردن خرید
    path('create/', views.order_create_view, name='order_create'),
]
