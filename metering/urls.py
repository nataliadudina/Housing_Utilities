from django.urls import path

from metering.apps import MeteringConfig
from metering.views import WaterMeterCreateAPIView, WaterMeterListAPIView, WaterMeterDetailAPIView

app_name = MeteringConfig.name

urlpatterns = [
    path("water/new_water_meter/", WaterMeterCreateAPIView.as_view(), name='water-meter-create'),
    path("water/", WaterMeterListAPIView.as_view(), name='water-meter-list'),
    path("water/<int:pk>/", WaterMeterDetailAPIView.as_view(), name='water-meter-read-update'),
]
