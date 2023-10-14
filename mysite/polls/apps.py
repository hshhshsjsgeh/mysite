"""
apps
"""
from django.apps import AppConfig


class PollsConfig(AppConfig):
    """
    app configuration to added in `settings.INSTALLED_APPS`
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'polls'
