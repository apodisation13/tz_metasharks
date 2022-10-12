import pytest
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from apps.core.models import Brand, Car, Color

QUANTITY = 10
COLOR_URL = "/api/v1/colors/"
BRAND_URL = "/api/v1/brands/"
CAR_URL = "/api/v1/cars/"


@pytest.mark.django_db
def test_get_colors(api_client, create_colors):
    colors = create_colors(_quantity=QUANTITY)
    response = api_client.get(COLOR_URL)
    assert response.status_code == HTTP_200_OK
    assert len(response.data) == len(colors)


@pytest.mark.django_db
def test_crud_color(api_client):
    response = api_client.get(COLOR_URL)
    assert response.status_code == HTTP_200_OK
    assert len(response.data) == 0
    response = api_client.post(COLOR_URL, {"name": "Зеленый"})
    assert response.status_code == HTTP_201_CREATED
    response = api_client.get(COLOR_URL)
    assert response.status_code == HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0].get("name") == "Зеленый"
    api_client.patch(f"{COLOR_URL}{response.data[0].get('id')}/", {"name": "Синий"})
    response = api_client.get(COLOR_URL)
    assert response.status_code == HTTP_200_OK
    assert response.data[0].get("name") == "Синий"
    response = api_client.delete(f"{COLOR_URL}{response.data[0].get('id')}/")
    assert response.status_code == HTTP_204_NO_CONTENT
    response = api_client.get(COLOR_URL)
    assert response.status_code == HTTP_200_OK
    assert len(response.data) == 0


@pytest.mark.django_db
def test_get_brands(api_client, create_brands):
    brands = create_brands(_quantity=QUANTITY)
    response = api_client.get(BRAND_URL)
    assert response.status_code == HTTP_200_OK
    assert len(response.data) == len(brands)


@pytest.mark.django_db
def test_crud_brand(api_client):
    response = api_client.get(BRAND_URL)
    assert response.status_code == HTTP_200_OK
    assert len(response.data) == 0
    response = api_client.post(BRAND_URL, {"name": "AUDI"})
    assert response.status_code == HTTP_201_CREATED
    response = api_client.get(BRAND_URL)
    assert response.status_code == HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0].get("name") == "AUDI"
    api_client.patch(f"{BRAND_URL}{response.data[0].get('id')}/", {"name": "BMW"})
    response = api_client.get(BRAND_URL)
    assert response.status_code == HTTP_200_OK
    assert response.data[0].get("name") == "BMW"
    response = api_client.delete(f"{BRAND_URL}{response.data[0].get('id')}/")
    assert response.status_code == HTTP_204_NO_CONTENT
    response = api_client.get(BRAND_URL)
    assert response.status_code == HTTP_200_OK
    assert len(response.data) == 0


@pytest.mark.django_db
def test_get_cars(api_client, create_cars):
    cars = create_cars(_quantity=QUANTITY)
    response = api_client.get(COLOR_URL)
    assert response.status_code == HTTP_200_OK
    assert len(response.data) == len(cars)


@pytest.mark.django_db
def test_crud_cars(api_client):
    brand = Brand.objects.create(name="AUDI")
    color = Color.objects.create(name="Зеленый")
    Car.objects.create(name="Запорожец", brand_id=brand.id, color_id=color.id)
    response = api_client.get(CAR_URL)
    assert response.status_code == HTTP_200_OK
    print(response.data)
    assert len(response.data) == 1
    assert response.data[0].get("name") == "Запорожец"
