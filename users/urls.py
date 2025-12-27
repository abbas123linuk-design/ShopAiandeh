# users/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # ثبت‌نام و پروفایل
    path('register/', views.register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/edit/', views.profile_edit_view, name='profile_edit'),

    # داشبورد
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('seller-dashboard/', views.seller_dashboard_view, name='seller_dashboard'),

    # ========== URL های جدید برای آدرس ==========
    path('addresses/', views.address_list_view, name='address_list'),
    path('addresses/add/', views.address_create_view, name='address_create'),
    path('addresses/<int:pk>/edit/', views.address_update_view, name='address_update'),
    path('addresses/<int:pk>/delete/', views.address_delete_view, name='address_delete'),
    # ============================================
]
