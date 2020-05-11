from rest_framework import serializers

from .models import FarmzoneUser


class FarmzoneUserSerializer(serializers.ModelSerializer):
    """Serializer for FarmzoneUser class."""

    class Meta:
        model = FarmzoneUser
        fields = '__all__'
