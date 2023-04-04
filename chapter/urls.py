from django.urls import path
from chapter.views import ListChapters


urlpatterns = [
    path('', ListChapters.as_view(), name='List Characters'),
    #path('<int:pk>/', CharacterID.as_view(), name='Character ID')
]
