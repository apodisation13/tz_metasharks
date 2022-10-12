from rest_framework.viewsets import ModelViewSet

from apps.orders.filters import OrderListFilter
from apps.orders.models import Order
from apps.orders.pagination import OrderResultSetPagination
from apps.orders.serializers import OrderSerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = OrderResultSetPagination
    ordering_fields = ["quantity"]  # ?ordering=-quantity DESC
    filterset_class = OrderListFilter  # ?car_brand=Audi
