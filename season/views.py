from rest_framework import generics
from .models import Season
from .serializers import SeasonSerialzer


class ListSeasons(generics.ListAPIView):
    queryset = Season.objects.all()
    serializer_class = SeasonSerialzer
