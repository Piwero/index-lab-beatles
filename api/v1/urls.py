from django.urls import path

from api.v1.song_ranking_endpoints import NonAuthenticatedSongViewSet

app_name = "v1"

urlpatterns = [
    path(
        "songs",
        NonAuthenticatedSongViewSet.as_view({"get": "list"}),
        name="non-auth-songs",
    ),
]
