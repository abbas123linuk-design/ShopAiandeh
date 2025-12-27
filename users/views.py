# users/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, AddressForm # AddressForm را وارد کنید
from .models import Address # Address را وارد کنید
from products.models import Product

# ... (ویوهای register, profile_edit, dashboard, seller_dashboard بدون تغییر)
def register_view(request):
    if request.user.is_authenticated: return redirect('dashboard')
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'ثبت‌نام با موفقیت انجام شد. سلام {user.username}!')
            return redirect('dashboard')
    else: form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
@login_required
def profile_edit_view(request):
    if request.method == 'POST':
        u_form, p_form = UserUpdateForm(request.POST, instance=request.user), ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save(); p_form.save()
            messages.success(request, 'پروفایل شما با موفقیت به‌روزرسانی شد!')
            return redirect('profile_edit')
    else: u_form, p_form = UserUpdateForm(instance=request.user), ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'users/profile_edit.html', {'u_form': u_form, 'p_form': p_form})
@login_required
def dashboard_view(request):
    if hasattr(request.user, 'profile') and request.user.profile.is_seller: return redirect('seller_dashboard')
    return render(request, 'users/customer_dashboard.html', {})
@login_required
def seller_dashboard_view(request):
    if not (hasattr(request.user, 'profile') and request.user.profile.is_seller): return redirect('dashboard')
    seller_products = Product.objects.filter(seller=request.user)
    context = {'total_products': seller_products.count(), 'total_sales': 0, 'recent_products': seller_products.order_by('-created_at')[:5]}
    return render(request, 'users/seller_dashboard.html', context)


# ========== ویوهای جدید برای مدیریت آدرس ==========

@login_required
def address_list_view(request):
    addresses = Address.objects.filter(user=request.user)
    return render(request, 'users/address_list.html', {'addresses': addresses})

@login_required
def address_create_view(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            messages.success(request, 'آدرس جدید با موفقیت اضافه شد.')
            return redirect('address_list')
    else:
        form = AddressForm()
    return render(request, 'users/address_form.html', {'form': form, 'page_title': 'افزودن آدرس جدید'})

@login_required
def address_update_view(request, pk):
    address = get_object_or_404(Address, pk=pk, user=request.user)
    if request.method == 'POST':
        form = AddressForm(request.POST, instance=address)
        if form.is_valid():
            form.save()
            messages.success(request, 'آدرس با موفقیت ویرایش شد.')
            return redirect('address_list')
    else:
        form = AddressForm(instance=address)
    return render(request, 'users/address_form.html', {'form': form, 'page_title': 'ویرایش آدرس'})

@login_required
def address_delete_view(request, pk):
    address = get_object_or_404(Address, pk=pk, user=request.user)
    if request.method == 'POST':
        address.delete()
        messages.success(request, 'آدرس با موفقیت حذف شد.')
        return redirect('address_list')
    return render(request, 'users/address_delete_confirm.html', {'address': address})

# ========================================================
