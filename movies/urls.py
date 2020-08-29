from django.urls import path
from movies import views
from django.urls import include

urlpatterns = [
    path('listmovies/', views.MoviesListView.as_view(), name='movie-list'),
]
