from django.contrib import admin
from .models import Song, Artiste, Lyric
# Register your models here.

@admin.register(Artiste)
class ArtisteAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'age']

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['title', 'artiste_id', 'date_released']

@admin.register(Lyric)
class LyricAdmin(admin.ModelAdmin):
    list_display = ['song_id']
