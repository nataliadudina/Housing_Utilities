from rest_framework import serializers

from metering.models import WaterMeter


class NewWaterMeterSerializer(serializers.ModelSerializer):
    """ Сериализатор для создания нового счетчика воды."""

    class Meta:
        model = WaterMeter
        fields = '__all__'


class WaterMeterSerializer(serializers.ModelSerializer):
    """ Сериализатор для представления счетчиков воды."""

    apartment_address = serializers.SerializerMethodField()
    apartment_number = serializers.SerializerMethodField()

    class Meta:
        model = WaterMeter
        fields = ['id', 'apartment_address', 'apartment_number', 'current_reading', 'previous_reading']

    def get_apartment_number(self, obj):
        """  Метод для получения номера квартиры."""
        return obj.apartment.number

    def get_apartment_address(self, obj):
        """ Метод для получения адреса квартиры."""
        from housing.serializers import HouseSerializer

        house_data = HouseSerializer(obj.apartment.house).data
        return f"{house_data['street']}, {house_data['building']}"
