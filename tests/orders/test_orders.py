import datetime
from random import choice, randint

import pytest
from django.conf import settings
from rest_framework.status import HTTP_200_OK, HTTP_204_NO_CONTENT

from apps.core.models import Brand, Car, Color
from apps.orders.models import Order

QUANTITY = 10
ORDER_URL = "/api/v1/orders/"
ORDERS_BY_COLOR_URL = "/api/v1/orders_by_color/"
ORDERS_BY_BRAND_URL = "/api/v1/orders_by_brand/"
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


@pytest.mark.django_db
def test_ordering_by_quantity(api_client):
    brand = Brand.objects.create(name="AUDI")
    color = Color.objects.create(name="Зеленый")
    car = Car.objects.create(name="Запорожец", brand_id=brand.id, color_id=color.id)
    for i in range(QUANTITY):
        quantity = randint(1, QUANTITY)
        Order.objects.create(car=car, quantity=quantity)
    response = api_client.get(f"{ORDER_URL}?ordering=-quantity")
    assert response.status_code == HTTP_200_OK
    results = response.data["results"]
    assert len(results) == settings.ORDERS_PER_PAGE
    assert response.data["count"] == QUANTITY
    for i in range(1, len(results)):
        assert results[i]["quantity"] <= results[i - 1]["quantity"]


@pytest.mark.django_db
def test_filtering_by_brand(api_client):
    brand_1 = Brand.objects.create(name="Audi")
    brand_2 = Brand.objects.create(name="Ford")
    color = Color.objects.create(name="Зеленый")
    car_1 = Car.objects.create(name="Запорожец", color_id=color.id, brand_id=brand_1.id)
    car_2 = Car.objects.create(name="Запорожец", color_id=color.id, brand_id=brand_2.id)
    for i in range(QUANTITY):
        Order.objects.create(quantity=QUANTITY, car=choice([car_1, car_2]))
    desired_brand = "Ford"
    response = api_client.get(f"{ORDER_URL}?car_brand={desired_brand}")
    assert response.status_code == HTTP_200_OK
    results = response.data["results"]
    for i in range(len(results)):
        assert results[i]["brand"] == desired_brand


@pytest.mark.django_db
def test_orders_by_color(api_client):
    color_1 = Color.objects.create(name="Зеленый")
    color_2 = Color.objects.create(name="Красный")
    brand = Brand.objects.create(name="AUDI")
    car_1 = Car.objects.create(name="Запорожец", color_id=color_1.id, brand_id=brand.id)
    car_2 = Car.objects.create(name="Запорожец", color_id=color_2.id, brand_id=brand.id)
    random_1 = randint(1, QUANTITY)
    random_2 = randint(1, QUANTITY)
    for i in range(random_1):
        Order.objects.create(quantity=QUANTITY, car=car_1)
    for i in range(random_2):
        Order.objects.create(quantity=QUANTITY, car=car_2)
    response = api_client.get(ORDERS_BY_COLOR_URL)
    assert response.status_code == HTTP_200_OK
    assert len(response.data) == 2
    assert response.data[0]["name"] == "Зеленый"
    assert response.data[0]["orders"] == random_1
    assert response.data[1]["name"] == "Красный"
    assert response.data[1]["orders"] == random_2


@pytest.mark.django_db
def test_orders_by_brand(api_client):
    color = Color.objects.create(name="Зеленый")
    brand_1 = Brand.objects.create(name="Audi")
    brand_2 = Brand.objects.create(name="Ford")
    car_1 = Car.objects.create(name="Запорожец", color_id=color.id, brand_id=brand_1.id)
    car_2 = Car.objects.create(name="Запорожец", color_id=color.id, brand_id=brand_2.id)
    random_1 = randint(1, QUANTITY)
    random_2 = randint(1, QUANTITY)
    for i in range(random_1):
        Order.objects.create(quantity=QUANTITY, car=car_1)
    for i in range(random_2):
        Order.objects.create(quantity=QUANTITY, car=car_2)
    response = api_client.get(ORDERS_BY_BRAND_URL)
    assert response.status_code == HTTP_200_OK
    assert len(response.data) == 2
    assert response.data[0]["name"] == "Audi"
    assert response.data[0]["orders"] == random_1
    assert response.data[1]["name"] == "Ford"
    assert response.data[1]["orders"] == random_2
