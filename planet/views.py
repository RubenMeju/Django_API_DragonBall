from rest_framework import generics
from .models import Planet
from .serializers import PlanetSerialzer


class ListPlanet(generics.ListAPIView):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerialzer
