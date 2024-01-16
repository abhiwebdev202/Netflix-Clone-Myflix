from django.urls import path
from .views import Home, ProfileList, MovieList, ProfileCreate, MovieDetail, PlayMovie #,ProfileView

app_name = 'myflixapp'

urlpatterns = [
    path('', Home.as_view(), name='Home'),
    #path('accounts/profile/', ProfileView.as_view(), name='profile'),
    path('accounts/profile/', ProfileList.as_view(), name="profile-list"),
    path('accounts/profile/create/', ProfileCreate.as_view(), name="profile-create"),
    path('watch/<str:profile_id>/', MovieList.as_view(), name="movie-list"),
    path('watch/detail/<str:movie_id>/', MovieDetail.as_view(), name="movie-detail"),
    path('watch/play/<str:movie_id>/', PlayMovie.as_view(), name="play-movie"),
]
