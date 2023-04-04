from rest_framework.views import APIView
from rest_framework import generics
from .models import Chapter
from .serializers import ChapterSerializer


class ListChapters(generics.ListAPIView):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer