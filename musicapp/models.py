from django.db import models
from datetime import datetime

# Create your models here.
class Artiste(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name


class Song(models.Model):

    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    date_released = models.DateField(auto_now_add=True)
    likes = models.IntegerField()

    def __str__(self):
        return f"{self.title} by {self.artiste_id.__str__()}"


class Lyric(models.Model):

    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return "Lyrics to {}".format(self.song_id.__str__())