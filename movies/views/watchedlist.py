from movies.serializer import MovieSerializer, WatchListSerializer
from movies.models import Movie, WatchList
from rest_framework import generics, permissions, status
from users.permissions import IsOwner
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist


class WatchedListView(generics.ListAPIView):
    """
    List all the watched movies
    """

    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsOwner]


    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user, watched=True)


class MovieWatchedListView(generics.CreateAPIView,
                           generics.DestroyAPIView):
    """
    Add movies to watched list and Delete movies from watched list
    """

    serializer_class = WatchListSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    
    def get_object(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except ObjectDoesNotExist:
            raise Http404

    def post(self, request, pk):
        movie = self.get_object(pk)
        user = self.request.user
        movie_item, created = WatchList.objects.update_or_create(movie=movie,
                                                                 owner=user,
                                                                 defaults={'watched': True})
        serializer = self.serializer_class(movie_item)
        return Response(serializer.data, status=200)


    def delete(self, request, pk):
        movie = self.get_object(pk)
        user = self.request.user
        try:
            list_item = WatchList.objects.get(movie=movie, owner=user, watched=True)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        list_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    