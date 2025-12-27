# orders/urls.py

from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    # مسیر برای خریدار: دیدن خریدهای خودش
    path('', views.order_list_view, name='order_list'),
    
    # مسیر برای فروشنده: دیدن سفارش‌های دریافتی
    path('seller/', views.seller_order_list_view, name='seller_order_list'),
]
