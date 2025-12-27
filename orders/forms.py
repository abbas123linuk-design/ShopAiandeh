# orders/forms.py

from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        # ما فقط نیاز داریم آدرس را از کاربر بگیریم
        # بقیه فیلدها (user, total_price) را در view ست می‌کنیم
        fields = ['address']
        labels = {
            'address': 'آدرس تحویل سفارش را انتخاب کنید'
        }
