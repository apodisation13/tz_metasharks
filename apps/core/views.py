from rest_framework.viewsets import ModelViewSet

from apps.core.models import Brand, Car, Color
from apps.core.serializers import BrandSerializer, CarSerializer, ColorSerializer


class ColorViewSet(ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class BrandViewSet(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class CarViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
