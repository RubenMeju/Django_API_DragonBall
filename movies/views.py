from rest_framework import generics
from .models import Movie
from .serializers import MovieSerializer


class ListMovies(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
