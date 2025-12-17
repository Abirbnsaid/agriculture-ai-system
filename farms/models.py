from django.db import models


class Farm(models.Model):
    name = models.CharField(max_length=100)
    size = models.FloatField()
    crop_type = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class FieldPlot(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, related_name="plots")
    area = models.FloatField()

    def __str__(self):
        return f"Plot {self.id}"
