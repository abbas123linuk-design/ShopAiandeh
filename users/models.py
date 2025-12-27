# users/models.py

from django.db import models
from django.contrib.auth.models import User
# دیگر نیازی به ایمپورت‌های سیگنال نیست

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="کاربر")
    is_seller = models.BooleanField(default=False, verbose_name="فروشنده است؟")
    
    def __str__(self):
        return f"پروفایل کاربر {self.user.username}"
        
    class Meta:
        verbose_name = "پروفایل"
        verbose_name_plural = "پروفایل‌ها"

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='addresses', verbose_name="کاربر")
    province = models.CharField(max_length=100, verbose_name="استان")
    city = models.CharField(max_length=100, verbose_name="شهر")
    postal_code = models.CharField(max_length=10, verbose_name="کد پستی")
    address_detail = models.TextField(verbose_name="آدرس دقیق")
    is_default = models.BooleanField(default=False, verbose_name="آدرس پیش‌فرض")

    def __str__(self):
        return f"{self.province}, {self.city}..."

    class Meta:
        verbose_name = "آدرس"
        verbose_name_plural = "آدرس‌ها"

# ========== نکته مهم: سیگنال‌ها کاملاً حذف شدند ==========
