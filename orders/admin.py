# orders/admin.py

from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']
    readonly_fields = ('price',)
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'address', 'is_paid', 'created_at']
    list_filter = ['is_paid', 'created_at']
    inlines = [OrderItemInline]
