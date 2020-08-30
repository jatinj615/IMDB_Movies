from rest_framework import viewsets, views, permissions
from movies.movie_script import get_movies
from movies.serializer import MovieSerializer
from movies.models import Movie
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from movies.tasks import store_movies_data


class StoreMoviesView(views.APIView):
    """
    Trigger Celery task to scrape and store movies in Database
    """

    serializer_class = MovieSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        url = self.request.data['imdb_url']
        store_movies_data.delay(url)
        return Response({'message': 'Storing movies in Background'},status=200)
        




    