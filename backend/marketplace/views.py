from rest_framework import viewsets

from .serializers import ProductsAdsSerializers
from .models import ProductsAds


# Create your views here.
# class ProductsAdsView(viewsets.ModelViewSet, generics.RetrieveUpdateDestroyAPIView):
class ProductsAdsView(viewsets.ModelViewSet):
    queryset = ProductsAds.objects.all()
    serializer_class = ProductsAdsSerializers
