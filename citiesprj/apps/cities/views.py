from django.shortcuts import render


from rest_framework import filters, viewsets

from .serializers import CitySerializer
from .models import City


class CityViewSet(viewsets.ModelViewSet):
    model = City
    serializer_class = CitySerializer
    queryset = City.objects.all()

