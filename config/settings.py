from django.contrib.messages import constants as message_constants
from pathlib import Path
import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY', default="django-insecure-@+ok!(=bgyt_!w=c5&fl554l9bsmz&d63!gz*7+gwyuj_4q=s-")

DEBUG = os.environ.get("DJANGO_DEBUG", default=True)

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",

    # third-party
    'embed_video',
    
    'core',
    'main',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ['templates'],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "main.context_processors.site_cart",
            ],
        },
    },
]

LOGIN_URL = '/login/'

ASGI_APPLICATION = "config.asgi.application"

WSGI_APPLICATION = "config.wsgi.application"

DATABASE_PROD = os.environ.get("DATABASE_PROD", default="0") == "1"

DATABASES = {
    "default": {
        'OPTIONS': {
            'options': '-c search_path=public'
        },
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get('DATABASE_NAME', default='jotun'),
        "USER": os.environ.get('DATABASE_USER', default='jotun'),
        "PASSWORD": os.environ.get('DATABASE_PASSWORD', default='ipOm70RVxhBIIfTSOBeL'),
        "HOST": os.environ.get('DATABASE_HOST', default='127.0.0.1'),
        "PORT": os.environ.get('DATABASE_PORT', default=5432),
    } if DATABASE_PROD else {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR/'media')

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

MESSAGE_TAGS = {
    message_constants.DEBUG: 'info',
    message_constants.INFO: 'info',
    message_constants.SUCCESS: 'success',
    message_constants.WARNING: 'warning',
    message_constants.ERROR: 'danger',
}

SITE_TITLE = "Learning site admin"
SITE_HEADER = "Learning administration"
INDEX_TITLE = "Dashboard administration"

PAYMENT_GATEWAY_USERNAME = os.environ.get("PAYMENT_GATEWAY_USERNAME", default='mwtest')
PAYMENT_GATEWAY_PASSWORD = os.environ.get("PAYMENT_GATEWAY_PASSWORD", default='WHaNFE5C3qlChqNbAzH4')
PAYMENT_GATEWAY_TERMINAL_ID = os.environ.get("PAYMENT_GATEWAY_TERMINAL_ID", default='111111')

PAYMENT_GATEWAY_PROD = os.environ.get("PAYMENT_GATEWAY_PROD", default="0") == "1"

PAYMENT_WEBHOOK_SECRET = os.environ.get("PAYMENT_WEBHOOK_SECRET", default="")
PAYMENT_FINISH_URL = os.environ.get("PAYMENT_FINISH_URL", default="http://127.0.0.1:8000/success/")
PAYMENT_NOTIFICATION_URL = os.environ.get("PAYMENT_NOTIFICATION_URL", default="http://127.0.0.1:8000/api/payment/webhook/")
PAYMENT_GATEWAY_URL = os.environ.get("PAYMENT_GATEWAY_URL", default="https://uat-sandbox-3ds-api.qi.iq")
USE_SIGNATURE_VERIFICATION = os.environ.get("USE_SIGNATURE_VERIFICATION", default=False) == "1"

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

CSRF_TRUSTED_ORIGINS = ['https://example.com', 'https://www.example.com',]
CSRF_ALLOWED_ORIGINS = ["https://example.com"]
CORS_ORIGINS_WHITELIST = ["https://example.com"]

AUTHENTICATION_BACKENDS = [
    'main.backends.PhoneEmailUsernameBackend',
    # 'django.contrib.auth.backends.ModelBackend',
]
