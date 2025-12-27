# products/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product
from .forms import ProductForm
from site_settings.models import Banner
from cart.forms import CartAddProductForm

# --- ویوهای عمومی ---

def homepage_view(request):
    products = Product.objects.all().order_by('-created_at')
    
    # لیستی از تمام بنرهای فعال را می‌گیریم و بر اساس تاریخ ایجاد مرتب می‌کنیم
    active_banners = Banner.objects.filter(is_active=True).order_by('created_at')

    # برای اشکال‌زدایی: این خط در ترمینال شما چاپ می‌شود
    print(f"--- Found {active_banners.count()} active banners ---")
    print(active_banners)

    context = {
        'products': products,
        'active_banners': active_banners,
    }
    return render(request, 'products/homepage.html', context)

def product_detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'products/product_detail.html', context)


# --- ویوهای داشبورد فروشنده ---
# (این بخش بدون تغییر و صحیح است)

@login_required
def seller_product_list_view(request):
    if not (hasattr(request.user, 'profile') and request.user.profile.is_seller):
        messages.error(request, "شما اجازه دسترسی به این صفحه را ندارید.")
        return redirect('dashboard')
    products = Product.objects.filter(seller=request.user)
    return render(request, 'products/seller_product_list.html', {'products': products})

@login_required
def seller_product_create_view(request):
    if not (hasattr(request.user, 'profile') and request.user.profile.is_seller):
        messages.error(request, "شما اجازه دسترسی به این صفحه را ندارید.")
        return redirect('dashboard')
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user
            product.save()
            messages.success(request, "محصول شما با موفقیت اضافه شد.")
            return redirect('products:seller_product_list')
    else:
        form = ProductForm()
    return render(request, 'products/seller_product_form.html', {'form': form, 'page_title': 'افزودن محصول جدید'})

@login_required
def seller_product_update_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if not (request.user == product.seller):
        messages.error(request, "شما اجازه ویرایش این محصول را ندارید.")
        return redirect('products:seller_product_list')
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "محصول شما با موفقیت ویرایش شد.")
            return redirect('products:seller_product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/seller_product_form.html', {'form': form, 'page_title': f'ویرایش محصول: {product.name}'})

@login_required
def seller_product_delete_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if not (request.user == product.seller):
        messages.error(request, "شما اجازه حذف این محصول را ندارید.")
        return redirect('products:seller_product_list')
    if request.method == 'POST':
        product.delete()
        messages.success(request, "محصول شما با موفقیت حذف شد.")
        return redirect('products:seller_product_list')
    return render(request, 'products/seller_product_delete_confirm.html', {'product': product})

# products/views.py
# ... (import های دیگر)
 # <--- فرم را وارد کنید

def product_detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart_product_form = CartAddProductForm() # <--- یک نمونه از فرم بسازید
    context = {
        'product': product,
        'cart_product_form': cart_product_form, # <--- فرم را به context اضافه کنید
    }
    return render(request, 'products/product_detail.html', context)
