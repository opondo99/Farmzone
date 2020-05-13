from rest_framework import viewsets
# from rest_framework import permissions

from .serializers import FarmzoneUserSerializer, FarmzoneUser


class FarmzoneUserViewSet(viewsets.ModelViewSet):
    # pylint: disable=missing-docstring

    queryset = FarmzoneUser.objects.all()
    serializer_class = FarmzoneUserSerializer
