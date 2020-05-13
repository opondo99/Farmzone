# pylint: skip-file

from rest_framework import viewsets
# from rest_framework import permissions

from .serializers import FarmzoneUserSerializer, FarmzoneUser


class FarmzoneUserViewSet(viewsets.ModelViewSet):
    """Viewset for create, retrieve, update, delete FarmzoneUser records."""

    queryset = FarmzoneUser.objects.all()
    serializer_class = FarmzoneUserSerializer
