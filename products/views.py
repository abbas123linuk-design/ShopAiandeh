# products/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product
from .forms import ProductForm

# --- ویوهای عمومی ---

def homepage_view(request):
    products = Product.objects.all().order_by('-created_at')
    context = {'products': products}
    return render(request, 'products/homepage.html', context)

def product_detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'products/product_detail.html', context)

# --- ویوهای داشبورد فروشنده ---

@login_required
def seller_product_list_view(request):
    # امنیت: مطمئن شو که کاربر یک فروشنده است
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
            # قبل از ذخیره، فروشنده را به صورت دستی ست می‌کنیم
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

    # امنیت: مطمئن شو که این محصول متعلق به همین فروشنده است
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
