from movies.serializer import MovieSerializer, WatchListSerializer
from movies.models import Movie, WatchList
from rest_framework import generics
from users.permissions import IsOwner


class MoviesListView(generics.ListAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        queryset = Movie.objects.all()
        title_match = self.request.query_params.get('title_match', None)
        if title_match is not None:
            queryset = queryset.filter(title__icontains=title_match)
        return queryset



# class WatchListView(generics.)
