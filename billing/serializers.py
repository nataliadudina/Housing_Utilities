from rest_framework import serializers

from billing.models import Tariff


class TariffSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели Tariff."""

    class Meta:
        model = Tariff
        fields = '__all__'
