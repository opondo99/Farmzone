"""Views module focuses on API views."""

from rest_framework import viewsets
from .models import ProductsAds
from .serializers import ProductsAdsSerializers


class ProductsAdsView(viewsets.ModelViewSet):
    """Handles the database objects access."""

    queryset = ProductsAds.objects.all()
    serializer_class = ProductsAdsSerializers
