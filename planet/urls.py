from django.urls import path
from planet.views import ListPlanet

urlpatterns = [
    path('', ListPlanet.as_view(), name='List Planet')
]
