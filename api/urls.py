from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('artiste/', views.artiste_list_api, name="artistes_api"),
    path('artiste/<int:id>/', views.artiste_detail_api, name="artiste_api"),
    path('song/', views.song_list_api, name="songs_api"),
    path('song/<int:id>/', views.song_detail_api, name="song_api"),
    path('lyric/', views.lyric_list_api, name="lyrics_api"),
    path('lyric/<int:id>', views.lyric_detail_api, name="lyric_api"),
]