from django.db import models


class Color(models.Model):
    """Модель цвета машин"""
    name = models.CharField(max_length=32,
                            blank=False, null=False,
                            unique=True,
                            verbose_name="Название цвета")

    def __str__(self):
        return f'{self.id} - {self.name}'


class Brand(models.Model):
    """Модель марок (брендов) машин"""
    name = models.CharField(max_length=32,
                            blank=False, null=False,
                            unique=True,
                            verbose_name="Марка машины")

    def __str__(self):
        return f'{self.id} - {self.name}'


class Car(models.Model):
    """Модель машины - название, марка (бренд), цвет"""
    name = models.CharField(max_length=64,
                            blank=False, null=False,
                            verbose_name="Название машины")
    brand = models.ForeignKey("Brand",
                              blank=False, null=False,
                              on_delete=models.PROTECT,
                              related_name="cars",
                              verbose_name="Марка машины")
    color = models.ForeignKey("Color",
                              blank=False, null=False,
                              on_delete=models.PROTECT,
                              related_name="cars",
                              verbose_name="Цвет")

    def __str__(self):
        return f"{self.id} - {self.name}, Марка {self.brand}, Цвет {self.color}"
