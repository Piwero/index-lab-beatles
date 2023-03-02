import pytest

from api.v1.song_ranking_endpoints import NonAuthenticatedSongSerializer
from songs.models import Song


@pytest.fixture
def song_1(db):
    return Song.objects.create(
        name="A Hard Day's Night",
        album="A Hard Day's Night",
        writer="John Lennon\nPaul McCartney",
        rank=15,
        year_release=1964,
        singer="John Lennon\n(with Paul McCartney)",
        song_time="02:32",
        spotify_streams="1,000,000",
        rolling_stone_rank=1,
        NME_rank=1,
        UG_views=1000000,
        UG_favourites=1000000,
    )


@pytest.fixture
def song_2(db):
    return Song.objects.create(
        name="I Should Have Known Better",
        album="Magical Mystery Tour",
        writer="Paul McCartney",
        rank=20,
        year_release=1966,
        singer="Paul McCartne)",
        song_time="02:32",
        spotify_streams="2,000,000",
        rolling_stone_rank=2,
        NME_rank=2,
        UG_views=2000000,
        UG_favourites=2000000,
    )


@pytest.fixture
def song_3(db):
    return Song.objects.create(
        name="Can't Buy Me Love",
        album="A Hard Day's Night",
        writer="John Lennon",
        rank=30,
        year_release=1966,
        singer="John Lennon",
        song_time="02:32",
        spotify_streams="3,000,000",
        rolling_stone_rank=3,
        NME_rank=3,
        UG_views=3000000,
        UG_favourites=3000000,
    )


@pytest.fixture
def all_songs(song_1, song_2, song_3):
    return Song.objects.all()


class TestRankingEndPoint:
    def test_serialize_song_name_for_non_authenticated_user(self, all_songs):
        serializer = NonAuthenticatedSongSerializer(all_songs, many=True)

        assert serializer.data[0]["name"] == "A Hard Day's Night"
        assert serializer.data[1]["name"] == "I Should Have Known Better"
        assert serializer.data[2]["name"] == "Can't Buy Me Love"

    def test_serialize_song_album_for_non_authenticated_user(self, all_songs):
        serializer = NonAuthenticatedSongSerializer(all_songs, many=True)

        assert serializer.data[0]["album"] == "A Hard Day's Night"
        assert serializer.data[1]["album"] == "Magical Mystery Tour"
        assert serializer.data[2]["album"] == "A Hard Day's Night"

    def test_serialize_song_rank_for_non_authenticated_user(self, all_songs):
        serializer = NonAuthenticatedSongSerializer(all_songs, many=True)

        assert serializer.data[0]["rank"] == 15
        assert serializer.data[1]["rank"] == 20
        assert serializer.data[2]["rank"] == 30
