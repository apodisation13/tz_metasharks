import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from apps.core.models import Brand, Car, Color


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def create_colors():
    def color_factory(*args, **kwargs):
        return baker.make(Color, *args, **kwargs)
    return color_factory


@pytest.fixture
def create_brands():
    def brand_factory(*args, **kwargs):
        return baker.make(Brand, *args, **kwargs)
    return brand_factory


@pytest.fixture
def create_cars():
    def car_factory(*args, **kwargs):
        return baker.make(Car, *args, **kwargs)
    return car_factory
