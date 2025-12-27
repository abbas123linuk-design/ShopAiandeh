# core/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from products import views as product_views

urlpatterns = [
    path('', product_views.homepage_view, name='homepage'),
    path('admin/', admin.site.urls),
    path('accounts/', include('users.urls')),
    path('products/', include('products.urls')),
    path('cart/', include('cart.urls', namespace='cart')), # <--- URL سبد خرید
    path('orders/', include('orders.urls', namespace='orders')),
    # (URL سفارش‌ها را بعدا اضافه می‌کنیم)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
