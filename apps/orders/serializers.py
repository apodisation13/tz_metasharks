from rest_framework import serializers

from apps.core.models import Brand, Color
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


class OrderByColorSerializer(serializers.ModelSerializer):
    """Сериализатор заказов по цветам"""
    orders = serializers.SerializerMethodField()

    class Meta:
        fields = ("name", "orders")
        model = Color

    def get_orders(self, color):
        orders = Order.objects.filter(car__color__name=color.name).all()
        return len(orders)


class OrderByBrandSerializer(serializers.ModelSerializer):
    """Сериализатор заказов по маркам машин"""
    orders = serializers.SerializerMethodField()

    class Meta:
        fields = ("name", "orders")
        model = Brand

    def get_orders(self, brand):
        orders = Order.objects.filter(car__brand__name=brand.name).all()
        return len(orders)
