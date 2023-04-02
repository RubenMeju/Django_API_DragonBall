from django.urls import path
from episode.views import ListEpisodes

urlpatterns = [
    path('', ListEpisodes.as_view(), name='List Seasons')
]
