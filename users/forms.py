# users/forms.py

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Address

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['province', 'city', 'postal_code', 'address_detail', 'is_default']
        labels = {
            'province': 'استان',
            'city': 'شهر',
            'postal_code': 'کد پستی',
            'address_detail': 'آدرس دقیق',
            'is_default': 'ثبت به عنوان آدرس پیش‌فرض',
        }

class UserRegisterForm(UserCreationForm):
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
            # اینجا ما به صراحت پروفایل را می‌سازیم
            # چون سیگنال حذف شده، دیگر هیچ تداخلی ممکن نیست
            Profile.objects.create(
                user=user,
                is_seller=self.cleaned_data.get('is_seller')
            )
        return user

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=False, label="آدرس ایمیل")
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        labels = {'first_name': 'نام', 'last_name': 'نام خانوادگی',}

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = []
