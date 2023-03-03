from django.urls import path

from api.v1.song_ranking_endpoints import SongRankingViewSet

app_name = "v1"

urlpatterns = [
    path(
        "songs",
        SongRankingViewSet.as_view(),
        name="songs-list",
    ),
]
