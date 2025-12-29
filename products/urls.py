# products/urls.py

from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    # --- URL های داشبورد فروشنده ---
    path('seller/', views.seller_product_list_view, name='seller_product_list'),
    path('seller/add/', views.seller_product_create_view, name='seller_product_create'),
    path('seller/<int:pk>/edit/', views.seller_product_update_view, name='seller_product_update'),
    path('seller/<int:pk>/delete/', views.seller_product_delete_view, name='seller_product_delete'),
    path('search/', views.search_view, name='search'),
    # --- URL های عمومی ---
    path('<int:pk>/', views.product_detail_view, name='product_detail'),
]
