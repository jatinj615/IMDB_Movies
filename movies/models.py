from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    rating = models.CharField(max_length=10, blank=True, default='')
    imdb_key = models.CharField(max_length=20, blank=True, default='')
    type_rating = models.CharField(max_length=10, blank=True, default='')
    duration = models.CharField(max_length=20, blank=True, default='')
    genre = models.CharField(max_length=50, blank=True, default='')
    release_date = models.CharField(max_length=100, blank=True, default='')


class WatchList(models.Model):
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    watched = models.BooleanField(default=False)
    


