from movies.serializer import MovieSerializer, WatchListSerializer
from movies.models import Movie, WatchList
from rest_framework import generics, permissions, status
from users.permissions import IsOwner
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response


class MovieListView(generics.ListAPIView):
    """
    List all the movies by search on movie title 
    """

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self):
        
        title_match = self.request.query_params.get('title_match', None)
        if title_match is not None:
            queryset = self.queryset.filter(title__icontains=title_match)
            return queryset
        return super().get_queryset()


class MovieDetailView(generics.RetrieveAPIView):
    """
    List single movie details
    """

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
