# site_settings/models.py
from django.db import models

class Banner(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان")
    subtitle = models.CharField(max_length=300, blank=True, null=True, verbose_name="زیرنویس")
    image = models.ImageField(upload_to='banners/', verbose_name="تصویر بنر")
    link = models.URLField(blank=True, null=True, verbose_name="لینک (اختیاری)")
    is_active = models.BooleanField(default=True, verbose_name="فعال باشد؟")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "بنر"
        verbose_name_plural = "بنرها"
