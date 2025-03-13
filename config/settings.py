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
            ],
        },
    },
]

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


AUTHENTICATION_BACKENDS = [
    'main.backends.PhoneEmailUsernameBackend',
    # 'django.contrib.auth.backends.ModelBackend',
]
