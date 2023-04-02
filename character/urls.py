from django.urls import path, include
from character.views import ListCharacters, CharacterID
urlpatterns = [
    path('', ListCharacters.as_view(), name='List Characters'),
    path('<int:pk>/', CharacterID.as_view(), name='Character ID')
]
