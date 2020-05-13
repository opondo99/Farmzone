"""Serializer class for model FarmzoneUser."""
# pylint: skip-file
# pylint: disable=D203

from rest_framework import serializers

from .models import FarmzoneUser


class FarmzoneUserSerializer(serializers.ModelSerializer):
    """Serializer for FarmzoneUser class."""

    class Meta:
        """Meta class for FarmzoneUserSerializer."""

        model = FarmzoneUser
        fields = '__all__'
