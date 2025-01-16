from django.shortcuts import render
from rest_framework import generics
from .models import UserPreference, Song, Artist, Genre
from .serializers import UserPreferenceSerializer, SongSerializer, ArtistSerializer, GenreSerializer

def index(request): 
    return render(request, 'recommendation/index.html')

def preferences(request): 
    return render(request, 'recommendation/preferences.html')

def recommendations(request):
    return render(request, 'recommendation/recommendations.html')

class UserPreferencesListCreate(generics.ListCreateAPIView):
    queryset = UserPreference.objects.all()
    serializer_class = UserPreferenceSerializer

class SongListCreate(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    
    def get_queryset(self):
        user_id = self.kwargs['user_id']
        user_preferences = UserPreference.objects.filter(user_id=user_id)
        preferred_genres = user_preferences.values_list('genre', flat=True)
        preferred_artists = user_preferences.values_list('artist', flat=True)
        return Song.objects.filter(genre__in=preferred_genres, artist__in=preferred_artists)

class ArtistListCreate(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class GenreListCreate(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer