from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from sensors.views import SensorReadingViewSet

router = DefaultRouter()
router.register(r"sensors", SensorReadingViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
