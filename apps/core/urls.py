from rest_framework.routers import DefaultRouter

from apps.core.views import BrandViewSet, CarViewSet, ColorViewSet

router = DefaultRouter()

router.register("colors", ColorViewSet, basename="colors")
router.register("brands", BrandViewSet, basename="brands")
router.register("cars", CarViewSet, basename="cars")

urlpatterns = router.urls
