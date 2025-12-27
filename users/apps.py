# users/apps.py

from django.apps import AppConfig

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    # متد ready را حذف کردیم چون دیگر سیگنالی نداریم
