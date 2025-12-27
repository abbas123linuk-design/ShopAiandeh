# users/admin.py
from django.contrib import admin
from .models import Profile, Address # Address را وارد کنید

admin.site.register(Profile)
admin.site.register(Address) # Address را در پنل ادمین ثبت کنید
