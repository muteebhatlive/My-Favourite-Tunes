from django.urls import path
from .views import *

urlpatterns = [
    path('songs/', song_list, name='song_list'),
    path('song/<int:song_id>/', song_detail, name='song_detail'),
    path('add_song/', add_song, name='add_song'),
    path('add_artist/', add_artist, name='add_artist'),
]