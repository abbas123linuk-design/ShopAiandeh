# core/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# این import اشتباه بود و باعث خطا می‌شد: from . import views
# import صحیح برای ویو صفحه اصلی از اپ 'products' است 👇
from products import views as product_views

urlpatterns = [
    # مسیر صفحه اصلی که از ویو داخل اپ 'products' استفاده می‌کند
    path('', product_views.homepage_view, name='homepage'),

    # مسیرهای دیگر
    path('admin/', admin.site.urls),
    path('accounts/', include('users.urls')),

    # ما یک مسیر جداگانه برای محصولات هم اضافه می‌کنیم تا تمیزتر باشد
    path('products/', include('products.urls')),
]

# این بخش برای نمایش عکس‌ها در حالت توسعه است و صحیح است
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
