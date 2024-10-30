import os
from pathlib import Path

# Base Directory
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Secret Key
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'your-default-secret-key')

# Debug Mode
DEBUG = os.environ.get('DJANGO_DEBUG', 'False') == 'True'

# Allowed Hosts
ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')

# Installed Apps
INSTALLED_APPS = [
    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Third-party apps
    'rest_framework',
    'rest_framework.authtoken',
    'django_celery_beat',
    'django_celery_results',
    
    # Project apps
    'src.users.apps.UsersConfig',
    'src.stocks.apps.StocksConfig',
    'src.analytics.apps.AnalyticsConfig',
    'src.notifications.apps.NotificationsConfig',
    'src.scraping.apps.ScrapingConfig',
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Custom middleware
    'src.core.middleware.QueryCountMiddleware',
]

# Root URL Configuration
ROOT_URLCONF = 'src.core.urls'

# Templates Configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'src' / 'templates'],
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

# WSGI and ASGI Applications
WSGI_APPLICATION = 'src.core.wsgi.application'
ASGI_APPLICATION = 'src.core.asgi.application'

# Database Configuration
# Placeholder since DynamoDB isn't directly supported by Django
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.dummy',
    }
}

# Password Validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 12,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/Jamaica'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static Files
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Default Auto Field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Custom User Model
AUTH_USER_MODEL = 'src.users.User'

# REST Framework Configuration
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}

# Celery Configuration
CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://localhost:6379/0')
CELERY_RESULT_BACKEND = 'django-db'
CELERY_BEAT_SCHEDULE = {
    'scrape_daily_stock_data': {
        'task': 'src.scraping.tasks.scrape_daily_stock_data',
        'schedule': crontab(hour=20, minute=0),  # Adjust to match 3 PM Jamaica Time (UTC-5)
    },
}
