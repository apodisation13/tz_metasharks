from rest_framework import serializers

from apps.orders.models import Order


class OrderSerializer(serializers.ModelSerializer):
    """Сериализатор Заказов - марка машины, цвет, название, количество, дата (по умолчанию текущая)"""
    class Meta:
        model = Order
        fields = ("id", "car", "quantity", "date")

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "quantity": instance.quantity,
            "date": instance.date,
            "brand": instance.car.brand.name,
            "color": instance.car.color.name,
            "name": instance.car.name,
        }
