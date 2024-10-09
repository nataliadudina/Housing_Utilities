from rest_framework import serializers

from metering.models import WaterMeter
from .models import House, Apartment


class BaseApartmentSerializer(serializers.ModelSerializer):
    """
    Сериализатор для квартиры.
    Предоставляет информацию о квартире, включая показания счётчика воды.
    """

    house = serializers.PrimaryKeyRelatedField(queryset=House.objects.all())
    water_meters = serializers.SerializerMethodField()

    class Meta:
        model = Apartment
        fields = ['id', 'house', 'number', 'area', 'owner', 'monthly_payment', 'water_meters']

    def get_water_meters(self, obj):
        """
        Метод для получения информации о счетчиках воды, связанных с данной квартирой.
        """
        water_meters = WaterMeter.objects.filter(apartment=obj).all()  # Получаем все счетчики воды текущей квартиры
        return [
            {
                'current_reading': meter.current_reading,
                'previous_reading': meter.previous_reading
            }
            for meter in water_meters
        ]

    def to_representation(self, instance):
        """
        Метод для настройки представления объекта квартиры.
        """
        representation = super().to_representation(instance)
        representation['house'] = str(instance.house)
        return representation


class SimpleApartmentSerializer(serializers.ModelSerializer):
    """
    Простой сериализатор для квартиры.
    Используется для сериализации только номера и площади квартиры.
    """

    class Meta:
        model = Apartment
        fields = ['number', 'area']


class HouseSerializer(serializers.ModelSerializer):
    """
    Сериализатор для дома.
    Предоставляет информацию о доме, включая список связанных квартир.
    """
    apartments = SimpleApartmentSerializer(many=True, read_only=True)

    class Meta:
        model = House
        fields = ['id', 'street', 'building', 'apartments']
