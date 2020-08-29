from django.urls import path
from movies import views
from django.urls import include

urlpatterns = [
    path('storemovies/', views.StoreMoviesView.as_view(), name='store-movie'),
    path('listmovies/', views.MoviesListView.as_view(), name='movie-list'),
    path('<int:pk>/watchlist/', views.MovieWatchListView.as_view(), name='add-watch-list'),
    path('watchlist/', views.MovieWatchListView.as_view(), name='watch-list'),
]
