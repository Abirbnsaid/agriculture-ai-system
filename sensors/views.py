from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import SensorReading
from .serializers import SensorReadingSerializer
from anomaly_ml.detector import detect_temperature


class SensorReadingViewSet(viewsets.ModelViewSet):
    queryset = SensorReading.objects.all()
    serializer_class = SensorReadingSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        instance = serializer.save()

        if instance.sensor_type == "temperature":
            status = detect_temperature(instance.value)
            instance.anomaly_status = status
            instance.save()

            print(f"[ML] Temp={instance.value} → {status}")
