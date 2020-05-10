from django.urls import path, include
from .views import ProductsAdsView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('ads', ProductsAdsView)

urlpatterns = [
    path('', include(router.urls))

]
"""
urlpatterns = [
    url(r'products/$', views.ProductsAdsView.as_view({'post': 'products'}), name='ads'),
"""
