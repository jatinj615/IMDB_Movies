from movies.serializer import MovieSerializer, WatchListSerializer
from movies.models import Movie, WatchList
from rest_framework import generics, permissions
from users.permissions import IsOwner
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response


class MovieListView(generics.ListAPIView):
    
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self):
        
        title_match = self.request.query_params.get('title_match', None)
        print(title_match)
        if title_match is not None:
            queryset = self.queryset.filter(title__icontains=title_match)
            return queryset
        return super().get_queryset()


class MovieDetailView(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]



class WatchListView(generics.ListAPIView):
    queryset = WatchList.objects.filter(watched=False)
    serializer_class = WatchListSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsOwner]



class MovieWatchListView(generics.CreateAPIView,
                         generics.DestroyAPIView):


    serializer_class = WatchListSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsOwner]


    def get_object(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist():
            return Http404


    def get(self, request):
        watchlist = WatchList.objects.filter(owner=self.request.user)
        serializer = self.serializer_class(watchlist, many=True)
        return Response(serializer.data)


    def post(self, request, pk):
        movie = self.get_object(pk)
        user = self.request.user
        print(type(user))
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(movie=movie, owner=user)
        print(serializer.errors)
        return Response(status=200)
    
    
    # def put(self, request, pk):
    #     watchlist_item = WatchList.objects.get(pk=pk)



