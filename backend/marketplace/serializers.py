"""
This module will handle all the object serialization for all the models
"""
from rest_framework import serializers

from .models import ProductsAds


class ProductsAdsSerializers(serializers.ModelSerializer):
    """ This class serializers and deserializes  python objects to json data. """

    class Meta:
        """ Meta class defines the fields to be serialized and it's model."""
        model = ProductsAds
        fields = ("ads_id", "pricing_id", "category_id", "user_id",
                  "Ads_content", "activity", "Ads_title")

    def update(self, instance, validated_data):
        """This method updates the products objects and save then to the DB."""
        instance.Ads_content = validated_data.get("Ads_content", instance.Ads_content)
        instance.activity = validated_data.get("activity", instance.activity)
        instance.Ads_title = validated_data.get("Ads_title", instance.Ads_title)
        instance.save()

        return instance
