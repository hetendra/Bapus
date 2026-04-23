from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-28j-inth&68j#dt7v%b3@c7zqpe^3h3vdor5d6*8j8@+&awnte'

# 🔴 IMPORTANT: Turn OFF in production
DEBUG = True

# ✅ Add your domain + IP
ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    '*',
    '13.233.224.64',
    'bapusrotlo.com',
    'www.bapusrotlo.com'
]

INSTALLED_APPS = [
    'Mainapp',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'Bapus.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        
        # ✅ Your templates path is fine
        'DIRS': [os.path.join(BASE_DIR, 'Mainapp', 'templates')],
        
        # 🔥 IMPORTANT FIX
        'APP_DIRS': True,
        
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Bapus.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True
USE_TZ = True

# ✅ FIXED (was wrong before)
STATIC_URL = '/static/'

# ✅ REQUIRED for Nginx
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# (optional but good)
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'