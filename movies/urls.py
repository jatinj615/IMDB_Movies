from django.urls import path
from movies import views
from django.urls import include

urlpatterns = [
    path('storemovies/', views.StoreMoviesView.as_view(), name='store-movie'),
    path('', views.MovieListView.as_view(), name='movie-list'),
    path('<int:pk>/', views.MovieDetailView.as_view(), name='movie-list'),
    path('<int:pk>/watchlist/', views.MovieWatchListView.as_view(), name='edit-watch-list'),
    path('watchlist/', views.WatchListView.as_view(), name='watch-list'),
    path('watched/', views.WatchedListView.as_view(), name='watched-list'),
    path('<int:pk>/watched/', views.MovieWatchedListView.as_view(), name='edit-watched-list'),
]
