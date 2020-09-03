from movies.serializer import MovieSerializer, WatchListSerializer
from movies.models import Movie, WatchList
from rest_framework import generics, permissions, status
from users.permissions import IsOwner
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist


class WatchListView(generics.ListAPIView):
    """
    List all the movies in watchlist
    """

    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsOwner]


    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user, watched=False)


class MovieWatchListView(generics.CreateAPIView,
                         generics.DestroyAPIView):
    """
    Add movies to watchlist and Delete movies from watchlist
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
        try:
            WatchList.objects.get(owner=user, movie=movie)
            return Response({'message': "Already watched"})
        except WatchList.DoesNotExist:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save(movie=movie, owner=user)
            return Response(serializer.data, status=200)
    

    def delete(self, request, pk):
        movie = self.get_object(pk)
        user = self.request.user
        try:
            list_item = WatchList.objects.get(movie=movie, owner=user, watched=False).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
