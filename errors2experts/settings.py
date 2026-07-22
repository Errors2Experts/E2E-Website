
"""
Django settings for errors2experts project.
"""
import os
from dotenv import load_dotenv
from pathlib import Path
import cloudinary
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

SECRET_KEY = 'django-insecure-5*2eyr04rscd0*_xjwxbo0x$(yqtzi49@2_$qx-52djqv28vs3'
DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'cloudinary_storage',
    'django.contrib.staticfiles',
    'cloudinary',
    'main',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'errors2experts.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'main.context_processors.latest_offer',
            ],
        },
    },
]

WSGI_APPLICATION = 'errors2experts.wsgi.application'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

print("DEBUG DATABASE_URL VALUE:", os.environ.get('DATABASE_URL'))

# Safe database configuration mapping
# DATABASES = {
#     'default': dj_database_url.config(
#         default=os.environ.get('DATABASE_PUBLIC_URL'),
#         conn_max_age=600,
#         ssl_require=True
#     )
# }


database_url = os.environ.get('DATABASE_URL')

if database_url:
    DATABASES = {
        'default': dj_database_url.parse(database_url, conn_max_age=600, ssl_require=True)
    }
# else:
#     # Safe temporary fallback if variable isn't loaded yet
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.sqlite3',
#             'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#         }
#     }

# # If it's still failing, explicitly parse or fallback to Railway's internal components
# if not DATABASES.get('default') or not DATABASES['default'].get('ENGINE'):
#     db_url = os.environ.get('DATABASE_URL')
#     if db_url:
#         DATABASES['default'] = dj_database_url.parse(db_url, conn_max_age=600, ssl_require=True)
#     else:
#         # Fallback directly to the internal hostname if variables aren't loading in the shell
#         DATABASES['default'] = {
#             'ENGINE': 'django.db.backends.postgresql',
#             'NAME': os.environ.get('PGDATABASE', 'railway'),
#             'USER': os.environ.get('PGUSER', 'postgres'),
#             'PASSWORD': os.environ.get('PGPASSWORD', ''),
#             'HOST': os.environ.get('PGHOST', 'postgres.railway.internal'),
#             'PORT': os.environ.get('PGPORT', '5432'),
#         }


AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'main/static')]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST_USER = 'errors2experts.official@gmail.com'
EMAIL_HOST_PASSWORD = 'otlivhwdqvdvkmwt'

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_TIMEOUT = 20

EMAIL_BACKEND = os.getenv(
    "EMAIL_BACKEND",
    "django.core.mail.backends.smtp.EmailBackend"
)

# EMAIL_HOST = os.getenv("EMAIL_HOST")
# EMAIL_PORT = int(os.getenv("EMAIL_PORT", 587))
# EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS") == "True"
# EMAIL_USE_SSL = os.getenv("EMAIL_USE_SSL") == "True"

# EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
# EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
ADMIN_NOTIFICATION_EMAIL = 'errors2experts.official@gmail.com'

# 1. Define them using os.getenv pointing to your environment variables correctly
CLOUDINARY_CLOUD_NAME = os.getenv("CLOUDINARY_CLOUD_NAME", "wnuppjlk")
CLOUDINARY_API_KEY = os.getenv("CLOUDINARY_API_KEY", "241645673172952")
CLOUDINARY_API_SECRET = os.getenv(
    "CLOUDINARY_API_SECRET", "NFGPUy3ZxDbQYEOwOpA5IYMf8AQ")

CLOUDINARY_STORAGE = {
    "CLOUD_NAME": CLOUDINARY_CLOUD_NAME,
    "API_KEY": CLOUDINARY_API_KEY,
    "API_SECRET": CLOUDINARY_API_SECRET,
}

# 2. Configure cloudinary using proper strings/variables
cloudinary.config(
    cloud_name=CLOUDINARY_CLOUD_NAME,
    api_key=CLOUDINARY_API_KEY,
    api_secret=CLOUDINARY_API_SECRET,
    secure=True
)

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

STORAGES = {
    "default": {
        "BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.StaticFilesStorage",
    },
}

# Fix for compatibility
STATICFILES_STORAGE = 'whitenoise.storage.StaticFilesStorage'

CSRF_TRUSTED_ORIGINS = [
    'https://errors2experts.up.railway.app',
]
