from rest_framework import viewsets

from housing.models import House, Apartment
from housing.serializers import HouseSerializer, BaseApartmentSerializer


class HouseViewSet(viewsets.ModelViewSet):
    """
    API эндпоинт для управления домами.

    Предоставляет CRUD операции для объектов House.
    Использует HouseSerializer для сериализации данных.
    """

    serializer_class = HouseSerializer
    queryset = House.objects.all()


class ApartmentViewSet(viewsets.ModelViewSet):
    """
    API эндпоинт для управления квартирами.

    Предоставляет CRUD операции для объектов Apartment.
    Использует ApartmentSerializer для сериализации данных.
    """

    serializer_class = BaseApartmentSerializer
    queryset = Apartment.objects.all()
