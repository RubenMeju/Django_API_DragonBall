from rest_framework.views import APIView
from rest_framework import generics
from .models import Character
from .serializers import CharacterSerializer


class ListCharacters(generics.ListAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer


class CharacterID(generics.RetrieveAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
