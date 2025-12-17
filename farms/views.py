from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Farm, FieldPlot
from .serializers import FarmSerializer, FieldPlotSerializer

class FarmViewSet(viewsets.ModelViewSet):
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer
    permission_classes = [AllowAny]

class FieldPlotViewSet(viewsets.ModelViewSet):
    queryset = FieldPlot.objects.all()
    serializer_class = FieldPlotSerializer
    permission_classes = [AllowAny]
