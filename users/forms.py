# users/forms.py

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

# فرم ثبت‌نام
class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, label="نام")
    last_name = forms.CharField(max_length=30, required=True, label="نام خانوادگی")
    # ایمیل را به صورت یک فیلد اختیاری تعریف می‌کنیم 👇
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


# فرم برای ویرایش اطلاعات مدل User
class UserUpdateForm(forms.ModelForm):
    # ایمیل را در فرم ویرایش هم به صورت اختیاری تعریف می‌کنیم 👇
    email = forms.EmailField(required=False, label="آدرس ایمیل")

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        labels = {
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
        }


# فرم برای ویرایش اطلاعات مدل Profile
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = []
