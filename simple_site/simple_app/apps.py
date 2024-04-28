from django.apps import AppConfig


class SimpleAppConfig(AppConfig):
    # For admin panel
    # verbose_name = "Товары"
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'simple_app'
