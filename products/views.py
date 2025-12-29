from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product
from .forms import ProductForm
from site_settings.models import Banner
from cart.forms import CartAddProductForm
from django.db.models import Q

# --- ویوهای عمومی ---

def homepage_view(request):
    # 1. محصولات شگفت‌انگیز: محصولاتی که "قیمت تخفیف" (discount_price) دارند
    # نکته: اگر هنوز مدل را آپدیت نکردی، این خط ارور می‌دهد. حتما مدل را طبق دستور قبلی آپدیت کن.
    try:
        amazing_products = Product.objects.filter(discount_price__isnull=False).exclude(discount_price=0).order_by('-created_at')[:10]
    except:
        # اگر هنوز دیتابیس آپدیت نشده، لیست خالی برگردان تا سایت بالا بیاید
        amazing_products = []

    # 2. جدیدترین محصولات (برای لیست پایین صفحه)
    latest_products = Product.objects.all().order_by('-created_at')[:12]
    
    # 3. بنرهای فعال
    active_banners = Banner.objects.filter(is_active=True).order_by('created_at')

    context = {
        'amazing_products': amazing_products,
        'latest_products': latest_products,
        'active_banners': active_banners,
    }
    return render(request, 'products/homepage.html', context)

def product_detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    # فرم افزودن به سبد خرید
    cart_product_form = CartAddProductForm()
    
    context = {
        'product': product,
        'cart_product_form': cart_product_form,
    }
    return render(request, 'products/product_detail.html', context)

# --- ویوهای داشبورد فروشنده ---

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
# این خط را به بالای فایل، کنار سایر import ها اضافه کن


# --- این تابع را به آخر فایل اضافه کن ---
def search_view(request):
    query = request.GET.get('q')
    products = []
    
    if query:
        # جستجو در نام محصول یا توضیحات
        products = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        ).order_by('-created_at')
    
    context = {
        'products': products,
        'query': query,
    }
    return render(request, 'products/search_results.html', context)
