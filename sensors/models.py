from django.db import models
from farms.models import FieldPlot

class SensorReading(models.Model):
    plot = models.ForeignKey(FieldPlot, on_delete=models.CASCADE)
    sensor_type = models.CharField(max_length=20)
    value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)


    anomaly_status = models.CharField(
        max_length=20,
        default="UNKNOWN"
    )

    def __str__(self):
        return f"{self.sensor_type} - {self.value} ({self.anomaly_status})"
