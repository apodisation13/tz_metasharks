from rest_framework.viewsets import ModelViewSet

from apps.core.models import Brand, Car, Color
from apps.core.serializers import BrandSerializer, CarSerializer, ColorSerializer


class ColorViewSet(ModelViewSet):
    """
    Эндпоинт цветов машин
    Роут /api/v1/colors/
    """
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class BrandViewSet(ModelViewSet):
    """
    Эндпоинт марок машин
    Роут /api/v1/brands/
    """
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class CarViewSet(ModelViewSet):
    """
    Эндпоинт машин: название машины, название цвета машины, название марки машины
    Роут /api/v1/cars/
    """
    queryset = Car.objects.all()
    serializer_class = CarSerializer
