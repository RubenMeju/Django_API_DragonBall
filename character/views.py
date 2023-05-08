from rest_framework import filters
from rest_framework.views import APIView
from rest_framework import generics
from .models import Character
from .serializers import CharacterSerializer


class ListCharacters(generics.ListAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class CharacterID(generics.RetrieveAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
