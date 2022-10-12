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
    color = ColorSerializer(many=False)
    brand = BrandSerializer(many=False)

    class Meta:
        fields = ("id", "name", "brand", "color")
        model = Car
