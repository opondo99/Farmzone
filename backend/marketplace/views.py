"""Views module focuses on API views."""

from rest_framework import viewsets

from .models import ProductsAds
from .serializers import ProductsAdsSerializers


# noqa
# noqa: D203, D211
class ProductsAdsView(viewsets.ModelViewSet):
    """Handles the database objects access."""

    queryset = ProductsAds.objects.all()
    serializer_class = ProductsAdsSerializers
