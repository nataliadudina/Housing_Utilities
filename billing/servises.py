from decimal import Decimal

from billing.models import Tariff
from housing.models import Apartment
from metering.models import WaterMeter


def save_monthly_payment(apartment, total_payment):
    """ Сохраняет общий платеж за месяц для указанной квартиры."""
    apartment.monthly_payment = total_payment
    apartment.save()
    return total_payment


def calculate_payment(apartment_id):
    """
    Рассчитывает общий платеж за квартиру по заданному идентификатору квартиры.

    Если месячный платеж равен нулю, выполняется первичный расчет, включая
    расчеты по счетчикам воды и платежи за содержание общего имущества.
    Если месячный платеж уже начислен, выполняется перерасчет, который включает
    только платежи по счетчикам воды.
    """
    # Получаем квартиру и тариф
    apartment = Apartment.objects.get(id=apartment_id)
    tariff = Tariff.objects.filter(apartment=apartment).first()
    if not tariff:
        raise ValueError(f"Tariff for apartment with id {apartment.id} does not exist.")

    # Получаем счетчики воды для квартиры
    water_meters = WaterMeter.objects.filter(apartment=apartment)

    # Рассчитываем первичный платёж за месяц
    if apartment.monthly_payment == 0:
        # Первичный расчёт
        water_payments = Decimal(0)
        for meter in water_meters:
            if meter.current_reading > meter.previous_reading:
                water_payment = Decimal(meter.current_reading - meter.previous_reading) * Decimal(tariff.water_tariff)
                water_payments += water_payment

        # Платежи за содержание общего имущества
        maintenance_payment = Decimal(apartment.area) * Decimal(tariff.common_property_maintenance_tariff)

        all_payments = water_payments + maintenance_payment

    # Делаем перерасчёт квартплаты
    else:
        water_payments = Decimal(0)
        for meter in water_meters:
            if meter.current_reading > meter.previous_reading:
                water_payment = Decimal(meter.current_reading - meter.previous_reading) * Decimal(tariff.water_tariff)
                water_payments += water_payment
        all_payments = water_payments + apartment.monthly_payment

    # Обновляем предыдущие показания
    for meter in water_meters:
        meter.previous_reading = meter.current_reading
        meter.save()

    # Сохраняем общий платеж в квартире
    return save_monthly_payment(apartment, all_payments)
