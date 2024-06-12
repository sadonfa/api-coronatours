from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.shortcuts import render

from tours.models import Tours
from tours.serializers import ToursSerializers


class TourApiViewSets(ModelViewSet):
    serializer_class = ToursSerializers
    queryset = Tours.objects.all()


class TourView(ModelViewSet):
    serializer_class = ToursSerializers
    queryset = Tours.objects.get(id=1)
