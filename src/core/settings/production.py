from .base import *

# Production-specific settings

DEBUG = False

ALLOWED_HOSTS += ['your-production-domain.com']

# Database configuration for production (DynamoDB via custom integration)
# Note: Django doesn't natively support DynamoDB, consider using a third-party backend or integrating via boto3.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.dummy',  # Placeholder
    }
}

# Security settings
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Static files settings
STATIC_ROOT = BASE_DIR / 'staticfiles'
