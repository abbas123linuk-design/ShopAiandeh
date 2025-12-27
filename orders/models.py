# orders/models.py

from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from users.models import Address

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders', verbose_name="کاربر")
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="آدرس")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    is_paid = models.BooleanField(default=False, verbose_name="پرداخت شده؟")
    total_price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name="مبلغ نهایی")

    class Meta:
        ordering = ('-created_at',)
        verbose_name = "سفارش"
        verbose_name_plural = "سفارش‌ها"

    def __str__(self):
        return f"سفارش {self.id} توسط {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', verbose_name="سفارش")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items', verbose_name="محصول")
    price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name="قیمت در زمان خرید")
    quantity = models.PositiveIntegerField(default=1, verbose_name="تعداد")

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity
