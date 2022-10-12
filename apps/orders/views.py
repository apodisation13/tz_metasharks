from rest_framework.viewsets import ModelViewSet

from apps.orders.models import Order
from apps.orders.serializers import OrderSerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
