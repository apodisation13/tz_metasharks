import django_filters

from apps.orders.models import Order


class OrderListFilter(django_filters.FilterSet):
    car_brand = django_filters.CharFilter(label="Car Brand Name", field_name="car__brand__name")

    class Meta:
        model = Order
        fields = ["car_brand"]
