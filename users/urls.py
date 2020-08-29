from django.urls import path
from users import views
from django.urls import include


urlpatterns = [
    path('signup/', views.CreateUserView.as_view(), name='user-signup'),
    path('login/', views.LoginView.as_view(), name='user-login'),
    path('check/', views.CheckView.as_view()),
]


