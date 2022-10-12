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
    # color = ColorSerializer(many=False)
    # brand = BrandSerializer(many=False)
    color = serializers.CharField(source="color.name")
    brand = serializers.CharField(source="brand.name")

    class Meta:
        fields = ("id", "name", "color", "brand")
        model = Car

    def create(self, validated_data):
        print(validated_data)
        color = Color.objects.filter(name=validated_data.pop("color")["name"]).first()
        brand = Brand.objects.filter(name=validated_data.pop("brand")["name"]).first()
        return Car.objects.create(**validated_data, color_id=color.id, brand_id=brand.id)
