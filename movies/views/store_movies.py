from rest_framework import viewsets, views, permissions
from movies.movie_script import get_movies
from movies.serializer import MovieSerializer
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication



class StoreMoviesView(views.APIView):

    serializer_class = MovieSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        url = self.request.data['imdb_url']
        movies = get_movies(url)
        for movie in movies:
            serializer = self.serializer_class(data=movie)
            if serializer.is_valid():
                serializer.save()
        
        return Response(status=200)
            




    