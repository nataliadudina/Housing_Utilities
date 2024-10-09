from django.urls import include, path
from rest_framework.routers import DefaultRouter

from housing.apps import HousingConfig
from housing.views import HouseViewSet, ApartmentViewSet

app_name = HousingConfig.name

router = DefaultRouter()
router.register(r"houses", HouseViewSet, basename="houses")
router.register(r"apartments", ApartmentViewSet, basename="apartments")

urlpatterns = [
    path("", include(router.urls)),
]
