"""App side of the API."""
from django.apps import AppConfig


# noqa: D212,D204,D404

class MarketplaceConfig(AppConfig):
    """
    MarketplaceConfig class interfaces this app with other apps.
    """

    name = 'backend.marketplace'
