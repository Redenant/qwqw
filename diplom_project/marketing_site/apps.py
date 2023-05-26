from django.apps import AppConfig
from django.apps import AppConfig


class MarketingSiteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'marketing_site'

    # def ready(self):
    #     import marketing_site.signals
