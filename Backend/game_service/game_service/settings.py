import os
from pathlib import Path
from datetime import timedelta

BASE_DIR = Path(__file__).resolve().parent.parent

ROOT_URLCONF = 'game_service.urls'

# Secret key directly provided here (change this in production)
SECRET_KEY = 'django-insecure-inf^k^znhee!2o$98hiz@-#v$fo57$d$n$+f+pmzf1ov(1h_jz'

DEBUG = True

ALLOWED_HOSTS = ['*']

# Installed apps (Include rest_framework and simplejwt)
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
    'channels',
    'game',  # your game app
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

# CORS settings (allow the frontend, authen_service, and game_service)
CORS_ALLOWED_ORIGINS = [
    'http://localhost:5173',  # Your frontend URL (Vite)
    'http://localhost:8000',  # authen_service URL
    'http://localhost:8001',  # game_service URL
]

CORS_ALLOW_CREDENTIALS = True

# REST framework settings for JWT Authentication
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

# JWT settings (using the same key as authen_service)
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),  # You can adjust the time
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ALGORITHM': 'HS256',  # Same algorithm as in authen_service
    'SIGNING_KEY': 'django-insecure-inf^k^znhee!2o$98hiz@-#v$fo57$d$n$+f+pmzf1ov(1h_jz',  # Same secret key as authen_service
}

# Redis channel layer settings (for WebSockets)
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('redis', 6379)],
        },
    },
}

# Database configuration (directly written here, no env vars)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ft_transcendence_db',
        'USER': 'ft_transcendence',
        'PASSWORD': 'ft_transcendence@42',
        'HOST': 'db',
        'PORT': '5432',
    }
}

# Static files settings
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# WebSocket & ASGI Configuration
ASGI_APPLICATION = 'game_service.asgi.application'

# Email Configuration (if needed)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'mailhog'  # Assuming Mailhog is used for testing
EMAIL_PORT = 1025
EMAIL_USE_TLS = False
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
DEFAULT_FROM_EMAIL = 'team1337@transcendence.com'

# Default auto field for primary keys
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Template settings (to fix admin issue)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # Add paths to any directories containing custom templates (optional)
        ],
        'APP_DIRS': True,  # Enable app template directories
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


