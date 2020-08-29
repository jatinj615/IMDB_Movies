from rest_framework import serializers
from django.contrib.auth.models import User
from movies.models import Movie, WatchList
from users.serializer import UserSerializer



class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ['id', 'title', 'rating', 'imdb_key', 'type_rating', 'duration', 'genre', 'release_date']
    

class WatchListSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    movie = serializers.CharField(source="movie.title", read_only=True)

    class Meta:
        model = WatchList
        fields = ['id', 'owner', 'movie', 'watched']

