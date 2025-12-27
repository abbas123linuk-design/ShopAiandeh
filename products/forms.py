# products/forms.py

from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        # ما فیلد 'seller' را اینجا نمی‌آوریم، چون به صورت خودکار
        # در view، کاربری که لاگین کرده به عنوان فروشنده ثبت می‌شود.
        fields = ['name', 'description', 'price', 'image']
        labels = {
            'name': 'نام محصول',
            'description': 'توضیحات کامل',
            'price': 'قیمت (تومان)',
            'image': 'تصویر اصلی محصول',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }
