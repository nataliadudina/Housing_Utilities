from django.db import models

from housing.models import Apartment


class Tariff(models.Model):
    """
    Модель для хранения информации о расчетах квартплаты.

    Атрибуты:
        apartment (ForeignKey): Связь с моделью Apartment для привязки к конкретной квартире.
        water_tariff (DecimalField): Тариф за воду.
        common_property_maintenance_tariff (DecimalField): Тариф за содержание общего имущества.
    """
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, related_name='payment_calculations')
    water_tariff = models.DecimalField(max_digits=10, decimal_places=2, help_text='Тариф за воду')
    common_property_maintenance_tariff = models.DecimalField(max_digits=10, decimal_places=2,
                                                             help_text='Тариф за содержание общего имущества')

    def __str__(self):
        return f'Расчёт квартплаты для квартиры №{self.apartment.number} по адресу {str(self.apartment.house)} за {self.month}'
