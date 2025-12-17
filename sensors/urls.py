from rest_framework.routers import DefaultRouter
from .views import SensorReadingViewSet

router = DefaultRouter()
router.register(r'sensors', SensorReadingViewSet)

urlpatterns = router.urls
