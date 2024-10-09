from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from billing.models import Tariff
from billing.serializers import TariffSerializer
from housing.models import Apartment
from billing.tasks import get_payment


class TariffViewSet(viewsets.ModelViewSet):
    """
    Представление для работы с тарифами.

    Этот класс предоставляет стандартные операции CRUD (создание, чтение,
    обновление и удаление) для модели Tariff. Использует
    TariffSerializer для сериализации данных.
    """
    queryset = Tariff.objects.all()
    serializer_class = TariffSerializer


class MonthlyPaymentCalculationView(APIView):
    """
    Представление для расчета месячной квартплаты.

    Этот класс позволяет выполнять расчет квартплаты для конкретной квартиры
    на основе её идентификатора. Запускает фоновую задачу для выполнения
    расчета и возвращает результат клиенту.
    """
    model = Apartment
    serializer_class = TariffSerializer

    def get_object(self, queryset=None):
        apartment_id = self.kwargs.get('apart_pk')
        return get_object_or_404(self.model, pk=apartment_id)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()

        try:
            # Запускаем задачу в фоновом режиме
            result = get_payment.delay(instance.id)

            # Ждем результата задачи и получаем его
            task_result = result.get()

            # Проверяем статус задачи
            if task_result.get("status") == 'success':
                return Response({"message": "Payment calculation completed successfully",
                                 "monthly_payment": task_result.get("monthly_payment")}, status=status.HTTP_200_OK)
            else:
                return Response({"error": str(task_result)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
