"""App side of the API."""

from django.apps import AppConfig


class MarketplaceConfig(AppConfig):
    """
    Interfaces this app with other apps.
    """

    name = 'backend.marketplace'
