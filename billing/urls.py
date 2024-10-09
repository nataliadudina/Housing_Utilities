from django.urls import path, include
from rest_framework.routers import DefaultRouter

from billing.apps import BillingConfig
from billing.views import TariffViewSet, MonthlyPaymentCalculationView

app_name = BillingConfig.name

router = DefaultRouter()
router.register(r"tariffs", TariffViewSet, basename="tariffs")

urlpatterns = [
    path("", include(router.urls)),
    path('billing/<int:apart_pk>/', MonthlyPaymentCalculationView.as_view(), name='calculate_monthly_payment'),
]
