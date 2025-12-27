# core/settings.py

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
# این کلید را مخفی نگه دارید و در حالت نهایی آن را از یک متغیر محیطی بخوانید
SECRET_KEY = 'django-insecure-YOUR-SECRET-KEY' # کلید شما ممکن است متفاوت باشد، آن را تغییر ندهید

# ==============================================================================
# مهم: تنظیمات حالت توسعه (Development) در مقابل حالت نهایی (Production)
# ==============================================================================
#
# هشدار امنیتی: حالت DEBUG را در محیط نهایی (آنلاین) True نگذارید!
#
# ما هنوز در حال توسعه روی کامپیوتر شخصی هستیم، پس این مقدار باید True باشد.
DEBUG = True

# این لیست مشخص می‌کند که چه آدرس‌هایی مجاز به سرویس دادن این سایت هستند.
# وقتی DEBUG=True است، نیازی به پر کردن این لیست نیست.
# وقتی DEBUG=False (حالت نهایی) می‌شود، این لیست **باید** پر شود.
ALLOWED_HOSTS = []

# مثال برای وقتی که سایت را آنلاین کردید:
# ALLOWED_HOSTS = ['www.my-shop.com', 'my-shop.com']
# ==============================================================================


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',  # برای نمایش زیبای اعداد (مثل قیمت)

    # My Apps (اپ‌های ما)
    'products.apps.ProductsConfig',
    'users.apps.UsersConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
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
        # این آدرس، پوشه قالب‌های عمومی در ریشه پروژه را به جنگو معرفی می‌کند
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/
LANGUAGE_CODE = 'fa-ir'
TIME_ZONE = 'Asia/Tehran'
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/
STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# --- تنظیمات سفارشی ما ---

# ۱. تنظیمات احراز هویت (Authentication)
LOGIN_URL = 'login' # آدرس صفحه لاگین سفارشی ما
LOGIN_REDIRECT_URL = 'dashboard' # بعد از لاگین موفق، به اینجا هدایت شو
LOGOUT_REDIRECT_URL = 'homepage' # بعد از خروج، به صفحه اصلی هدایت شو

# ۲. تنظیمات فایل‌های آپلود شده توسط کاربر (Media)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

