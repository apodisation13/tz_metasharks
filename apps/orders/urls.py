from rest_framework.routers import DefaultRouter

from apps.orders.views import OrderByBrandViewSet, OrderByColorViewSet, OrderViewSet

router = DefaultRouter()
# список всех заказов, пагинация, сортировка по количеству, фильтр по марке машины: get, get one, post, patch, delete
router.register("orders", OrderViewSet, basename="orders")
# список заказов: цвет + количество заказов этого цвета: get, get one
router.register("orders_by_colors", OrderByColorViewSet, basename="orders_by_colors")
# список заказов: марка + количество заказов этой марки: get, get one
router.register("orders_by_brand", OrderByBrandViewSet, basename="orders_by_brand")

urlpatterns = router.urls
