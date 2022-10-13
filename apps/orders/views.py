from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from apps.core.models import Brand, Color
from apps.orders.filters import OrderListFilter
from apps.orders.models import Order
from apps.orders.pagination import OrderResultSetPagination
from apps.orders.serializers import OrderByBrandSerializer, OrderByColorSerializer, OrderSerializer


class OrderViewSet(ModelViewSet):
    """
    Эндпоинт заказов: количество, дата, название машины, марка, цвет
    Роут: /api/v1/orders/
    Возможна сортировка по количеству заказов ?ordering=-quantity
    Возможен фильтр заказов по марке ?car_brand=Audi
    Пагинация на N элементов на странице (настраивается в config/settings/)
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = OrderResultSetPagination
    ordering_fields = ["quantity"]  # ?ordering=-quantity DESC
    filterset_class = OrderListFilter  # ?car_brand=Audi


class OrderByColorViewSet(ReadOnlyModelViewSet):
    """
    Эндпоинт заказов по цветам: цвет и количество заказанных авто этого цвета
    Роут /api/v1/orders_by_color/
    """
    queryset = Color.objects.all()
    serializer_class = OrderByColorSerializer


class OrderByBrandViewSet(ReadOnlyModelViewSet):
    """
    Эндпоинт заказов по маркам: марка и количество заказанных авто этой марки
    Роут /api/v1/orders_by_brand/
    """
    queryset = Brand.objects.all()
    serializer_class = OrderByBrandSerializer
