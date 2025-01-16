from django.db import models
from django.contrib.auth.models import User

class Artist(models.Model):
    name = models.CharField(max_length=100, blank=False, unique=True, db_index=True)
    
    class Meta:
        verbose_name = "Artist"
        verbose_name_plural = "Artists" 
    
    def __str__(self):
        return self.name
    
class Genre(models.Model):
    name = models.CharField(max_length=100, blank=False, unique=True, db_index=True)

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"
    
    def __str__(self):
        return self.name

class UserPreference(models.Model):
    user  = models.ForeignKey(User, on_delete = models.CASCADE, related_name='preferences')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    song = models.CharField(max_length=100, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.song}"

class Song(models.Model):
    title = models.CharField(max_length=100, blank=False)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    recommendation_score = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-recommendation_score', 'title']
    
    def __str__(self):
        return self.title
    
    def update_recommendation_score(self, new_score):
        self.recommendation_score = new_score
        self.save()
