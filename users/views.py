# users/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# این ویو، کاربر را بر اساس نوع حساب کاربری (عادی یا فروشنده)
# به داشبورد مربوطه هدایت می‌کند.
@login_required
def dashboard_view(request):
    # چک می‌کنیم آیا کاربر پروفایل فروشندگی دارد یا نه
    if hasattr(request.user, 'profile') and request.user.profile.is_seller:
        return redirect('seller_dashboard')
    
    # اگر فروشنده نبود، داشبورد زیبای کاربر عادی را به او نمایش می‌دهیم
    context = {}
    return render(request, 'users/customer_dashboard.html', context)


# این ویو، داشبورد مخصوص فروشندگان را نمایش می‌دهد
@login_required
def seller_dashboard_view(request):
    # این یک لایه امنیتی مهم است.
    # اگر کاربر عادی سعی کند به این صفحه بیاید، او را به داشبورد خودش برمی‌گردانیم.
    if not (hasattr(request.user, 'profile') and request.user.profile.is_seller):
        return redirect('dashboard')
        
    context = {'message': 'این داشبورد فروشنده است. به زودی آن را کامل خواهیم کرد.'}
    # فعلا برای داشبورد فروشنده از همان قالب پایه استفاده می‌کنیم تا بعدا برایش یک قالب شیک بسازیم
    return render(request, 'users/base.html', context)

# users/views.py
# ... (import های قبلی)
from .forms import UserUpdateForm, ProfileUpdateForm # فرم‌ها را وارد کنید
from django.contrib import messages # برای نمایش پیام موفقیت

@login_required
def profile_edit_view(request):
    if request.method == 'POST':
        # فرم‌ها را با داده‌های ارسال شده از طرف کاربر پر می‌کنیم
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, instance=request.user.profile) # فایل‌ها را هم در نظر بگیر
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'پروفایل شما با موفقیت به‌روزرسانی شد!')
            return redirect('profile_edit') # کاربر را به همین صفحه برمی‌گردانیم تا نتیجه را ببیند

    else: # اگر درخواست GET بود
        # فرم‌ها را با اطلاعات فعلی کاربر پر می‌کنیم
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile_edit.html', context)
# users/views.py
# ... (import های قبلی)
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import login # <--- برای لاگین خودکار

def register_view(request):
    # اگر کاربر از قبل لاگین کرده بود، او را به داشبورد هدایت کن
    if request.user.is_authenticated:
        return redirect('dashboard')
        
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save() # فرم سفارشی ما، هم User و هم Profile را ذخیره می‌کند
            login(request, user) # کاربر جدید را به صورت خودکار لاگین کن
            messages.success(request, f'ثبت‌نام با موفقیت انجام شد. سلام {user.username}!')
            return redirect('dashboard') # او را به داشبورد هدایت کن
    else:
        form = UserRegisterForm()
    
    return render(request, 'users/register.html', {'form': form})
