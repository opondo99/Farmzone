from rest_framework import serializers
from .models import ProductsAds


class ProductsAdsSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductsAds
        fields = ("ads_id", "pricing_id", "category_id", "user_id",
                  "Ads_content", "activity", "Ads_title")

    def update(self, instance, validated_data):
        instance.Ads_content = validated_data.get("Ads_content", instance.Ads_content)
        instance.activity = validated_data.get("activity", instance.activity)
        instance.Ads_title = validated_data.get("Ads_title", instance.Ads_title)
        instance.save()

        return instance
