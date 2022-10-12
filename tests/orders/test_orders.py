import datetime
from random import randint

import pytest
from django.conf import settings
from rest_framework.status import HTTP_200_OK, HTTP_204_NO_CONTENT

from apps.core.models import Brand, Car, Color
from apps.orders.models import Order

QUANTITY = 10
ORDER_URL = "/api/v1/orders/"
DATE = "2022-10-12T14:39:14.554Z"


@pytest.mark.django_db
def test_get_orders(api_client):
    response = api_client.get(ORDER_URL)
    assert response.status_code == HTTP_200_OK
    assert len(response.data["results"]) == 0
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
    assert len(response.data["results"]) == 2


@pytest.mark.django_db
def test_factory_orders(api_client, create_orders):
    orders = create_orders(_quantity=QUANTITY)
    response = api_client.get(ORDER_URL)
    assert response.status_code == HTTP_200_OK
    assert len(response.data["results"]) == settings.ORDERS_PER_PAGE
    assert response.data["count"] == len(orders)


@pytest.mark.django_db
def test_crud_orders(api_client, create_orders):
    orders = create_orders(_quantity=QUANTITY)
    response = api_client.get(ORDER_URL)
    assert response.status_code == HTTP_200_OK
    assert response.data["count"] == len(orders)
    order = orders[0]
    new_quantity = 13
    response = api_client.patch(f"{ORDER_URL}{order.id}/", {"quantity": new_quantity})
    order = Order.objects.filter(pk=response.data["id"]).first()
    assert order.quantity == new_quantity
    response = api_client.get(ORDER_URL)
    assert response.status_code == HTTP_200_OK
    assert response.data["count"] == len(orders)
    order_to_delete = Order.objects.first()
    print(order_to_delete.pk, "PK")
    response = api_client.delete(f"{ORDER_URL}{order_to_delete.pk}/")
    assert response.status_code == HTTP_204_NO_CONTENT
    response = api_client.get(ORDER_URL)
    assert response.status_code == HTTP_200_OK
    assert response.data["count"] == len(orders) - 1
