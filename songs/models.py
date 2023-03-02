from django.db import models


class Song(models.Model):
    name = models.CharField(max_length=80)
    album = models.CharField(max_length=80)
    writer = models.CharField(max_length=80)
    rank = models.IntegerField()
    year_release = models.IntegerField()
    singer = models.CharField(max_length=80)
    song_time = models.CharField(max_length=5)
    spotify_streams = models.CharField(max_length=80)
    rolling_stone_rank = models.IntegerField()
    NME_rank = models.IntegerField()
    UG_views = models.IntegerField()
    UG_favourites = models.IntegerField()
