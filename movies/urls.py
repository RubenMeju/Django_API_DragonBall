from django.urls import path
from movies.views import ListMovies

urlpatterns = [
    path('', ListMovies.as_view(), name='List movies')
]
