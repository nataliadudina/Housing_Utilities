from django.db import models

from housing.models import Apartment


class WaterMeter(models.Model):
    """
    Модель для представления счетчиков воды.

    Атрибуты:
        apartment (ForeignKey): Связь с моделью Apartment, указывает на принадлежащую квартиру.
        current_reading (IntegerField): Текущее показание счетчика воды.
        previous_reading (IntegerField): Предыдущее показание счетчика воды.
    """

    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, related_name='apartment_water_meters')
    current_reading = models.IntegerField(help_text='Текущее показание счетчика', default=0)
    previous_reading = models.IntegerField(help_text='Предыдущее показание счетчика', default=0)

    def __str__(self):
        return f'Счетчик воды для квартиры {self.apartment.number} по адресу {str(self.apartment.house)}'

    class Meta:
        verbose_name = 'Счетчик воды'
        verbose_name_plural = 'Счетчики воды'
