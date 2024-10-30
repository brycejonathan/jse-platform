from .base import *

# Development-specific settings

DEBUG = True

ALLOWED_HOSTS += ['localhost', '127.0.0.1']

# Database configuration for development (SQLite for simplicity)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Static files settings
STATICFILES_DIRS = [BASE_DIR / 'src' / 'static']
