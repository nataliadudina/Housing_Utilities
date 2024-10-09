from django.db import models


class House(models.Model):
    """
        Модель для представления дома.

        Attributes:
            street (CharField): Улица, где находится дом.
            building (IntegerField): Номер здания.

        Methods:
            __str__: Возвращает строковое представление дома.
    """

    street = models.CharField(max_length=100)
    building = models.IntegerField()

    def __str__(self):
        return f'{self.street}, {self.building}'

    class Meta:
        verbose_name = "Дом"
        verbose_name_plural = "Дома"
        unique_together = (('street', 'building'),)


class Apartment(models.Model):
    """
        Модель для представления квартиры.

        Attributes:
            house (ForeignKey): Связь с моделью House.
            number (IntegerField): Номер квартиры.
            area (FloatField): Площадь квартиры в квадратных метрах.
            owner (CharField): Владелец квартиры.
            monthly_payment (DecimalField): Квартплата за месяц.
    """
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='apartments')
    number = models.IntegerField(unique=True)
    area = models.FloatField(help_text='Площадь квартиры в квадратных метрах')
    owner = models.CharField(max_length=255)
    monthly_payment = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f'{self.house}, {self.number}'

    class Meta:
        verbose_name = "Квартира"
        verbose_name_plural = "Квартиры"
