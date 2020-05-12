""" This is the admin section of the API """


from django.contrib import admin

from .models import ProductsAds


admin.site.register(ProductsAds)
