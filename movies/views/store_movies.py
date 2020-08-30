from rest_framework import viewsets, views, permissions
from movies.movie_script import get_movies
from movies.serializer import MovieSerializer
from movies.models import Movie
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication



class StoreMoviesView(views.APIView):

    serializer_class = MovieSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    # def get_object(self, imdb_key):
    #     try:
    #         return Movie.objects.get(imdb_key=imdb_key)
    #     except Movie.DoesNotExist():
    #         return None


    def post(self, request):
        url = self.request.data['imdb_url']
        movies = get_movies(url)
        for data in movies:
            movie = Movie.objects.filter(imdb_key=data['imdb_key'])
            if movie:
                serializer = self.serializer_class(movie[0], data=data)
            else:
                serializer = self.serializer_class(data=data)
            if serializer.is_valid():
                serializer.save()
        
        return Response(status=200)
            




    