from django.test import SimpleTestCase
from django.urls import reverse, resolve
from movies.views import MovieDetailView, MovieListView, MovieWatchedListView, MovieWatchListView, WatchedListView, WatchListView, StoreMoviesView


class TestUrls(SimpleTestCase):

    def test_store_movies_url(self):
        url = reverse('store-movie')
        self.assertEquals(resolve(url).func.view_class, StoreMoviesView)

    def test_movie_list_url(self):
        url = reverse('movie-list')
        self.assertEquals(resolve(url).func.view_class, MovieListView)

    def test_movie_detail_url(self):
        url = reverse('movie-detail', args=[1])
        self.assertEquals(resolve(url).func.view_class, MovieDetailView)

    def test_movie_add_watchlist_url(self):
        url = reverse('edit-watch-list', args=[1])
        self.assertEquals(resolve(url).func.view_class, MovieWatchListView)
    
    def test_watchlist_url(self):
        url = reverse('watch-list')
        self.assertEquals(resolve(url).func.view_class, WatchListView)
    
    def test_movie_add_watchedlist_url(self):
        url = reverse('edit-watched-list', args=[1])
        self.assertEquals(resolve(url).func.view_class, MovieWatchedListView)
    
    def test_movie_watchedlist_url(self):
        url = reverse('watched-list')
        self.assertEquals(resolve(url).func.view_class, WatchedListView)