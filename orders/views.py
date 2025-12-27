# orders/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem

@login_required
def order_list_view(request):
    """
    نمایش لیست سفارش‌های کاربر عادی (خریدار)
    """
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'orders/order_list.html', {'orders': orders})

@login_required
def seller_order_list_view(request):
    """
    نمایش لیست سفارش‌های دریافتی برای فروشنده
    """
    # 1. چک کردن اینکه کاربر حتماً فروشنده باشد
    if not (hasattr(request.user, 'profile') and request.user.profile.is_seller):
        return redirect('dashboard')
    
    # 2. پیدا کردن تمام آیتم‌هایی که:
    #    - محصولشان متعلق به این فروشنده است (product__seller=request.user)
    #    - (اختیاری) سفارششان پرداخت شده است (order__is_paid=True) -> فعلا کامنت شده
    
    seller_items = OrderItem.objects.filter(
        product__seller=request.user
    ).order_by('-order__created_at')

    return render(request, 'orders/seller_order_list.html', {'seller_items': seller_items})
