from django.db import models
from django.contrib.auth.models import User

# لیست دسته‌بندی‌های مشابه دیجی‌کالا
CATEGORY_CHOICES = (
    ('digital', 'کالای دیجیتال'),
    ('fashion', 'مد و پوشاک'),
    ('home', 'خانه و آشپزخانه'),
    ('beauty', 'زیبایی و سلامت'),
    ('toys', 'اسباب بازی'),
    ('other', 'سایر'),
)

class Product(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="فروشنده")
    
    # --- فیلدهای اصلی ---
    name = models.CharField(max_length=200, verbose_name="نام محصول")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other', verbose_name="دسته‌بندی")
    description = models.TextField(verbose_name="توضیحات")
    
    # --- قیمت و تخفیف ---
    price = models.DecimalField(max_digits=12, decimal_places=0, verbose_name="قیمت اصلی (تومان)")
    discount_price = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True, verbose_name="قیمت با تخفیف (اختیاری)")
    
    image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name="تصویر اصلی")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")

    # محاسبه درصد تخفیف برای نمایش در دایره قرمز
    def get_discount_percent(self):
        if self.discount_price and self.price > 0:
            return int(100 - (self.discount_price / self.price * 100))
        return 0

    # قیمت نهایی برای نمایش (اگر تخفیف دارد، آن را برگردان، وگرنه قیمت اصلی)
    def get_current_price(self):
        return self.discount_price if self.discount_price else self.price

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
