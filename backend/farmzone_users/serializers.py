"""Serializer class for model FarmzoneUser."""

from rest_framework import serializers

from .models import FarmzoneUser


class FarmzoneUserSerializer(serializers.ModelSerializer):
    # pylint: disable=missing-docstring

    class Meta:
        # pylint: disable=missing-docstring
        # pylint: disable=D106

        model = FarmzoneUser
        fields = '__all__'
