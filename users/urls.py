# users/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('seller-dashboard/', views.seller_dashboard_view, name='seller_dashboard'),
    path('register/', views.register_view, name='register'),
    # URL جدید برای ویرایش پروفایل 👇
    path('profile/edit/', views.profile_edit_view, name='profile_edit'),
]
