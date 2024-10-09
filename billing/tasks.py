from celery import shared_task

from billing.servises import calculate_payment
from housing.models import Apartment


@shared_task
def get_payment(apartment_id):
    """
    Фоновая задача для расчета месячного платежа за квартиру по ее идентификатору.

    Получает квартиру по заданному идентификатору, вызывает функцию расчета
    платежа и возвращает результат. Если возникает ошибка, возвращает сообщение
    об ошибке.
    """
    try:
        apartment = Apartment.objects.get(pk=apartment_id)
        payment = calculate_payment(apartment.pk)

        return {"status": "success", "monthly_payment": float(payment)}
    except Exception as e:
        return {"error": str(e)}
