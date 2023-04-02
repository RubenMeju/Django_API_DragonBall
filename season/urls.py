from django.urls import path
from season.views import ListSeasons

urlpatterns = [
    path('', ListSeasons.as_view(), name='List Seasons')
]
