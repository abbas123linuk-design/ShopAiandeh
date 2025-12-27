# orders/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from users.models import Address

@login_required
def order_create_view(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.total_price = cart.get_total_price()
            order.save()
            
            # حالا برای هر آیتم در سبد خرید، یک OrderItem بساز
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # سبد خرید را پاک کن
            cart.clear()
            
            # (در آینده کاربر را به صفحه تشکر یا درگاه پرداخت هدایت می‌کنیم)
            return render(request, 'orders/order_created.html', {'order': order})
    else:
        form = OrderCreateForm()
        # به فرم فقط آدرس‌های مربوط به کاربر فعلی را پاس بده
        form.fields['address'].queryset = Address.objects.filter(user=request.user)

    return render(request, 'orders/order_create.html', {'cart': cart, 'form': form})


# --- ویوهای قبلی (بدون تغییر) ---

@login_required
def order_list_view(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'orders/order_list.html', {'orders': orders})

@login_required
def seller_order_list_view(request):
    if not (hasattr(request.user, 'profile') and request.user.profile.is_seller):
        return redirect('dashboard')
    seller_items = OrderItem.objects.filter(product__seller=request.user).order_by('-order__created_at')
    return render(request, 'orders/seller_order_list.html', {'seller_items': seller_items})
