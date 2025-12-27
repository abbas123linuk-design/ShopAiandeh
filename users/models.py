# users/models.py
from django.db import models
from django.contrib.auth.models import User # مدل کاربر پیش‌فرض جنگو

class Profile(models.Model):
    # این یک ارتباط یک-به-یک بین کاربر جنگو و پروفایل ما ایجاد می‌کنه
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="کاربر")
    is_seller = models.BooleanField(default=False, verbose_name="فروشنده است؟")
    
    # می‌توانید فیلدهای دیگری هم اضافه کنید:
    # bio = models.TextField(blank=True, null=True, verbose_name="بیوگرافی")
    # avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name="آواتار")

    def __str__(self):
        return f"پروفایل کاربر {self.user.username}"
        
    class Meta:
        verbose_name = "پروفایل"
        verbose_name_plural = "پروفایل‌ها"
