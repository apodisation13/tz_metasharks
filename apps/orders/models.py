from django.db import models
from django.utils import timezone

from apps.core.models import Car


class Order(models.Model):
    car = models.ForeignKey(Car,
                            related_name="orders",
                            blank=False, null=False,
                            verbose_name="Модель авто",
                            on_delete=models.PROTECT)
    quantity = models.IntegerField(default=1, verbose_name="Количество")
    date = models.DateTimeField(default=timezone.now, verbose_name="Дата оформления заказ")

    def __str__(self):
        return f"{self.id} - {self.car}, количество {self.quantity}, {self.date}"

    class Meta:
        ordering = ['-id']
