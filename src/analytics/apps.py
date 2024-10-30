from django.apps import AppConfig

class AnalyticsConfig(AppConfig):
    default_auto_field= 'django.db.models.BigAutoField'
    name='src.scraping'
    verbose_name='Data Scraping Service'