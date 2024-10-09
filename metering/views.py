from rest_framework import generics

from metering.models import WaterMeter
from metering.serializers import WaterMeterSerializer, NewWaterMeterSerializer


class WaterMeterCreateAPIView(generics.CreateAPIView):
    """
    API представление для создания нового счетчика воды.

    Метод POST принимает данные о новом счетчике воды и сохраняет их в базу данных.
    Используется NewWaterMeterSerializer для сериализации входящих данных и создания нового объекта WaterMeter.
    """
    queryset = WaterMeter.objects.all()
    serializer_class = NewWaterMeterSerializer


class WaterMeterListAPIView(generics.ListAPIView):
    """
    API представление для получения списка всех счетчиков воды.

    Метод GET возвращает список всех существующих счетчиков воды.
    Используется WaterMeterSerializer для сериализации каждого объекта WaterMeter в JSON.

    """
    queryset = WaterMeter.objects.all()
    serializer_class = WaterMeterSerializer


class WaterMeterDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API представление для получения, обновления и удаления информации о счетчике воды.

    Методы:
    GET: Получение детальной информации о конкретном счетчике воды.
    PUT/PATCH: Обновление информации о существующем счетчике воды.
    DELETE: Удаление выбранного счетчика воды из базы данных.

    Используется WaterMeterSerializer для сериализации данных при получении, обновлении и удалении.

    Attributes:
        queryset (QuerySet): Все существующие счетчики воды в базе данных.
        serializer_class (Serializer): WaterMeterSerializer для сериализации данных при операциях CRUD.
    """
    queryset = WaterMeter.objects.all()
    serializer_class = WaterMeterSerializer
