# pylint: disable=W,C,R
from rest_framework import serializers
from .models import FarmzoneUser


class FarmzoneUserSerializer(serializers.ModelSerializer):

    class Meta:
        """Create auth token after creating a user."""

        model = FarmzoneUser
        fields = '__all__'
