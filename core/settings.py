# core/settings.py
from pathlib import Path
import os
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-YOUR-SECRET-KEY'
DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    # My Apps
    'products.apps.ProductsConfig',
    'users.apps.UsersConfig',
    'site_settings.apps.SiteSettingsConfig',
    'orders.apps.OrdersConfig', # <--- اپ جدید سفارش‌ها
    'cart.apps.CartConfig',     # <--- اپ جدید سبد خرید
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware', # Session middleware is crucial
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart', # <--- اضافه کردن context processor سبد خرید
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

DATABASES = { 'default': { 'ENGINE': 'django.db.backends.sqlite3', 'NAME': BASE_DIR / 'db.sqlite3', } }
AUTH_PASSWORD_VALIDATORS = [ {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',}, {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',}, {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',}, {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',}, ]
LANGUAGE_CODE = 'fa-ir'
TIME_ZONE = 'Asia/Tehran'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'dashboard'
LOGOUT_REDIRECT_URL = 'homepage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# شناسه سبد خرید در session
CART_SESSION_ID = 'cart'
