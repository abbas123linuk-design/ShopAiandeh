# products/admin.py

from django.contrib import admin
from .models import Product, ProductImage # ProductImage را هم وارد کنید

# این کلاس، نحوه نمایش فرم آپلود عکس‌ها را مشخص می‌کند
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1  # به صورت پیش‌فرض، جای آپلود 1 عکس اضافه را نشان بده
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'description')
    
    # این خط، جادوی اصلی است!
    inlines = [ProductImageInline] # <--- این خط را اضافه کنید
