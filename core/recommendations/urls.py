from django.urls import path
from .views import index, preferences, recommendations, UserPreferencesListCreate, SongListCreate, ArtistListCreate, GenreListCreate

urlpatterns = [
    path('', index, name='index'),
    path('preferences/', preferences, name='preferences'),
    path('recommendations/', recommendations, name='recommendations'),
    path('api/preferences/', UserPreferencesListCreate.as_view(), name='user-preferences'),  # Corrección aquí
    path('api/songs/', SongListCreate.as_view(), name='songs'),
    path('api/artists/', ArtistListCreate.as_view(), name='artists'),  # Añadido para artistas
    path('api/genres/', GenreListCreate.as_view(), name='genres'),  # Añadido para géneros
    path('api/recommendations/<int:user_id>/', SongListCreate.as_view(), name='recommendations'),  # Corrección aquí
]