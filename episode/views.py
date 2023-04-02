from rest_framework import generics
from .models import Episode
from .serializers import EpisodeSerialzer


class ListEpisodes(generics.ListAPIView):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerialzer
