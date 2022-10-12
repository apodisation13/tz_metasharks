import pytest
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

QUANTITY = 10
COLOR_URL = "/api/v1/colors/"


@pytest.mark.django_db
def test_get_colors(api_client, create_colors):
    colors = create_colors(_quantity=QUANTITY)
    response = api_client.get(COLOR_URL)
    assert response.status_code == HTTP_200_OK
    assert len(response.data) == len(colors)


@pytest.mark.django_db
def test_crud_color(api_client, create_colors):
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
