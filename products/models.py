# products/models.py

from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    # این فیلد باید حتما اینجا باشد
    seller = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="فروشنده")
    
    name = models.CharField(max_length=200, verbose_name="نام محصول")
    description = models.TextField(verbose_name="توضیحات")
    price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name="قیمت (تومان)")
    image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name="تصویر اصلی")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"
        ordering = ['-created_at']

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images', verbose_name="محصول")
    image = models.ImageField(upload_to='product_gallery/', verbose_name="تصویر")

    def __str__(self):
        return f"تصویر برای {self.product.name}"

    class Meta:
        verbose_name = "تصویر محصول"
        verbose_name_plural = "تصاویر محصولات"
