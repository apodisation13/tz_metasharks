from rest_framework import serializers

from apps.core.models import Brand, Car, Color


class ColorSerializer(serializers.ModelSerializer):
    """Сериализатор для модели цвета машин, отдает id и name (название цвета)"""
    class Meta:
        fields = ("id", "name")
        model = Color


class BrandSerializer(serializers.ModelSerializer):
    """Сериализатор для модели марки машин, отдает id и name (название марки)"""
    class Meta:
        fields = ("id", "name")
        model = Brand


class CarSerializer(serializers.ModelSerializer):
    """Сериализатор для модели цвета машин, отдает id, name (название машины), её цвет color и марку brand"""
    class Meta:
        fields = ("id", "name", "color", "brand")
        model = Car

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "name": instance.name,
            "color": instance.color.name,
            "brand": instance.brand.name,
        }
