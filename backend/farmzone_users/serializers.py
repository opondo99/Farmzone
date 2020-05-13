"""Serializer class for model FarmzoneUser."""
# pylint: skip-file

from rest_framework import serializers

from .models import FarmzoneUser


class FarmzoneUserSerializer(serializers.ModelSerializer):
    """Serializer for FarmzoneUser class."""

    class Meta:
        """Meta class."""

        model = FarmzoneUser
        fields = '__all__'
