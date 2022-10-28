from django.db import models

# Create your models here.
class Artiste(models.Model):

    first_name = models.CharField()
    last_name = models.CharField()
    age = models.IntegerField()


class Song(models.Model):

    Artiste = models.ForeignKey(Artiste, on_delete=models.PROTECT)
    title = models.CharField()
    date_released = models.DateField()
    likes = models.IntegerField()
    artiste_id = models.IntegerField()


class Lyric(models.Model):

    Song = models.ForeignKey(Song, on_delete=models.CASCADE)
    content = models.CharField()
    song_id = models.IntegerField()