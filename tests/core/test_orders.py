import datetime
from random import randint

import pytest
from rest_framework.status import HTTP_200_OK

from apps.core.models import Brand, Car, Color
from apps.orders.models import Order

ORDER_URL = "/api/v1/orders/"
DATE = "2022-10-12T14:39:14.554Z"


@pytest.mark.django_db
def test_get_cars(api_client):
    response = api_client.get(ORDER_URL)
    assert response.status_code == HTTP_200_OK
    assert len(response.data) == 0
    brand = Brand.objects.create(name="AUDI")
    color = Color.objects.create(name="Зеленый")
    car = Car.objects.create(name="Запорожец", brand_id=brand.id, color_id=color.id)
    quantity = randint(1, 10)
    order = Order.objects.create(car=car, quantity=quantity)
    assert datetime.datetime.now().second - order.date.second < 2  # ну вот тут только так - что не более 2сек разница
    order = Order.objects.create(car=car, quantity=quantity, date=DATE)
    assert order.date == DATE
    response = api_client.get(ORDER_URL)
    assert response.status_code == HTTP_200_OK
    assert len(response.data) == 2
