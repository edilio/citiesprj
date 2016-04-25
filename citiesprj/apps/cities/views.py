from rest_framework import filters, viewsets

from .serializers import CitySerializer
from .models import City


class CityViewSet(viewsets.ModelViewSet):
    model = City
    serializer_class = CitySerializer
    queryset = City.objects.all()
    filter_backends = (filters.SearchFilter, filters.OrderingFilter, filters.DjangoFilterBackend)
    search_fields = ('zip_code', 'city')
    ordering_fields = ('zip_code', 'city')
    filter_fields = ('state',)

