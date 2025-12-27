# users/forms.py

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Address # Address را وارد کنید

# ========== فرم جدید برای آدرس ==========
class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        # ما فیلد 'user' را نمی‌آوریم چون به صورت خودکار ست می‌شود
        fields = ['province', 'city', 'postal_code', 'address_detail', 'is_default']
        labels = {
            'province': 'استان',
            'city': 'شهر',
            'postal_code': 'کد پستی (۱۰ رقمی، بدون خط تیره)',
            'address_detail': 'آدرس دقیق، پلاک و واحد',
            'is_default': 'ثبت به عنوان آدرس پیش‌فرض',
        }
# ========================================

class UserRegisterForm(UserCreationForm):
    # ... (این کلاس بدون تغییر)
    first_name = forms.CharField(max_length=30, required=True, label="نام")
    last_name = forms.CharField(max_length=30, required=True, label="نام خانوادگی")
    email = forms.EmailField(required=False, label="آدرس ایمیل (اختیاری)")
    is_seller = forms.BooleanField(required=False, label="به عنوان فروشنده ثبت‌نام می‌کنم")
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email',)
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            user.profile.is_seller = self.cleaned_data.get('is_seller')
            user.profile.save()
        return user

class UserUpdateForm(forms.ModelForm):
    # ... (این کلاس بدون تغییر)
    email = forms.EmailField(required=False, label="آدرس ایمیل")
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        labels = {'first_name': 'نام', 'last_name': 'نام خانوادگی',}

class ProfileUpdateForm(forms.ModelForm):
    # ... (این کلاس بدون تغییر)
    class Meta:
        model = Profile
        fields = []
