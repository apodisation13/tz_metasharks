from rest_framework.routers import DefaultRouter

from apps.core.views import BrandViewSet, CarViewSet, ColorViewSet

router = DefaultRouter()

# список цветов машин: get, get one, post, patch, delete
router.register("colors", ColorViewSet, basename="colors")
# список марок машин: get, get one, post, patch, delete
router.register("brands", BrandViewSet, basename="brands")
# список машин: get, get one, post, patch, delete
router.register("cars", CarViewSet, basename="cars")

urlpatterns = router.urls
