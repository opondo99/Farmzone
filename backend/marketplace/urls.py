"""Urls file handles  the API urls."""

from django.urls import path, include

from rest_framework import routers

from .views import ProductsAdsView

router = routers.DefaultRouter()
router.register('ads', ProductsAdsView)

urlpatterns = [
    path('', include(router.urls))

]
