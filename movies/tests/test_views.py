from django.test import Client, TestCase
from django.urls import reverse
from movies.models import Movie, WatchList
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status


class TestMovieView(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.store_movie_url = reverse('store-movie')
        self.list_movie_url = reverse('movie-list')
        self.detail_movie_url = reverse('movie-detail', args=[1])
        self.edit_watch_list_url = reverse('edit-watch-list', args=[1])
        self.watch_list_url = reverse('watch-list')
        self.edit_watched_list_url = reverse('edit-watched-list', args=[1])
        self.watched_list_url = reverse('watched-list')
        self.credentials = {'username': 'trainman',
                            'password': 'trainman'}
        self.movie_object = {'title': 'dark night',
                             'rating': '8.4',
                             'imdb_key': '1234',
                             'type_rating': 'U',
                             'duration': '1hr 25mins',
                             'genre': 'Thriller',
                             'release_date': '24 sept 2014'}
        self.user = User.objects.create_user(**self.credentials)
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token '+ self.token.key)

    
    def test_store_movies_POST(self):

        response = self.client.post(self.store_movie_url, {'imdb_url': 'example/url'})
        self.assertEquals(response.status_code, status.HTTP_200_OK)


    def test_list_movies_GET(self):
        
        response = self.client.get(self.list_movie_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

        response = self.client.get(self.list_movie_url, {'title_match': 'title'})
        self.assertEquals(response.status_code, status.HTTP_200_OK)


    def test_detail_movies_GET(self):

        response = self.client.get(self.list_movie_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
    
    
    def test_watchlist_GET(self):
        response = self.client.get(self.watch_list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    
    def test_edit_watchlist_POST_DELETE(self):

        Movie.objects.create(**self.movie_object)
        response = self.client.post(self.edit_watch_list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)   

        response = self.client.delete(self.edit_watch_list_url)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)


    def test_watchedlist_GET(self):
        response = self.client.get(self.watched_list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    
    def test_edit_watchedlist_POST_DELETE(self):

        Movie.objects.create(**self.movie_object)
        response = self.client.post(self.edit_watched_list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)   

        response = self.client.delete(self.edit_watched_list_url)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)




    