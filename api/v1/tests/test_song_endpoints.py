import pytest
from django.contrib.auth.models import User
from rest_framework.reverse import reverse

from api.v1.song_ranking_endpoints import (
    AuthenticatedSongSerializer,
    NonAuthenticatedSongSerializer,
    SongRankingViewSet,
)
from songs.models import Song


@pytest.fixture
def user(db):
    return User.objects.create_user(username="test_user", password="test_password")


@pytest.fixture
def logged_in_client(client, user):
    client.force_login(user)
    return client


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

    def test_non_authenticated_user_can_get_list_of_songs_with_name(
        self, all_songs, client
    ):
        response = client.get(reverse("api:v1:songs-list"))

        assert response.status_code == 200, response.data
        assert response.json()[0]["name"] == "A Hard Day's Night"
        assert response.json()[1]["name"] == "I Should Have Known Better"
        assert response.json()[2]["name"] == "Can't Buy Me Love"

    def test_non_authenticated_user_can_get_list_of_songs_with_album(
        self, all_songs, client
    ):
        response = client.get(reverse("api:v1:songs-list"))

        assert response.status_code == 200, response.data
        assert response.json()[0]["album"] == "A Hard Day's Night"
        assert response.json()[1]["album"] == "Magical Mystery Tour"
        assert response.json()[2]["album"] == "A Hard Day's Night"

    def test_non_authenticated_user_can_get_list_of_songs_with_rank(
        self, all_songs, client
    ):
        response = client.get(reverse("api:v1:songs-list"))

        assert response.status_code == 200, response.data
        assert response.json()[0]["rank"] == 15
        assert response.json()[1]["rank"] == 20
        assert response.json()[2]["rank"] == 30

    def test_serialize_song_name_for_authenticated_user(self, all_songs):
        serializer = AuthenticatedSongSerializer(all_songs, many=True)

        assert serializer.data[0]["name"] == "A Hard Day's Night"
        assert serializer.data[1]["name"] == "I Should Have Known Better"
        assert serializer.data[2]["name"] == "Can't Buy Me Love"

    def test_serialize_song_album_for_authenticated_user(self, all_songs):
        serializer = AuthenticatedSongSerializer(all_songs, many=True)

        assert serializer.data[0]["album"] == "A Hard Day's Night"
        assert serializer.data[1]["album"] == "Magical Mystery Tour"
        assert serializer.data[2]["album"] == "A Hard Day's Night"

    def test_serialize_song_rank_for_authenticated_user(self, all_songs):
        serializer = AuthenticatedSongSerializer(all_songs, many=True)

        assert serializer.data[0]["rank"] == 15
        assert serializer.data[1]["rank"] == 20
        assert serializer.data[2]["rank"] == 30

    def test_serialize_song_writer_for_authenticated_user(self, all_songs):
        serializer = AuthenticatedSongSerializer(all_songs, many=True)

        assert serializer.data[0]["writer"] == "John Lennon\nPaul McCartney"
        assert serializer.data[1]["writer"] == "Paul McCartney"
        assert serializer.data[2]["writer"] == "John Lennon"

    def test_serialize_song_year_release_for_authenticated_user(self, all_songs):
        serializer = AuthenticatedSongSerializer(all_songs, many=True)

        assert serializer.data[0]["year_release"] == 1964
        assert serializer.data[1]["year_release"] == 1966
        assert serializer.data[2]["year_release"] == 1966

    def test_serialize_song_singer_for_authenticated_user(self, all_songs):
        serializer = AuthenticatedSongSerializer(all_songs, many=True)

        assert serializer.data[0]["singer"] == "John Lennon\n(with Paul McCartney)"
        assert serializer.data[1]["singer"] == "Paul McCartne)"
        assert serializer.data[2]["singer"] == "John Lennon"

    def test_serialize_song_song_time_for_authenticated_user(self, all_songs):
        serializer = AuthenticatedSongSerializer(all_songs, many=True)

        assert serializer.data[0]["song_time"] == "02:32"
        assert serializer.data[1]["song_time"] == "02:32"
        assert serializer.data[2]["song_time"] == "02:32"

    def test_serialize_song_spotify_streams_for_authenticated_user(self, all_songs):
        serializer = AuthenticatedSongSerializer(all_songs, many=True)

        assert serializer.data[0]["spotify_streams"] == "1,000,000"
        assert serializer.data[1]["spotify_streams"] == "2,000,000"
        assert serializer.data[2]["spotify_streams"] == "3,000,000"

    def test_serialize_song_rolling_stone_rank_for_authenticated_user(self, all_songs):
        serializer = AuthenticatedSongSerializer(all_songs, many=True)

        assert serializer.data[0]["rolling_stone_rank"] == 1
        assert serializer.data[1]["rolling_stone_rank"] == 2
        assert serializer.data[2]["rolling_stone_rank"] == 3

    def test_serialize_song_NME_rank_for_authenticated_user(self, all_songs):
        serializer = AuthenticatedSongSerializer(all_songs, many=True)

        assert serializer.data[0]["NME_rank"] == 1
        assert serializer.data[1]["NME_rank"] == 2
        assert serializer.data[2]["NME_rank"] == 3

    def test_serialize_song_UG_views_for_authenticated_user(self, all_songs):
        serializer = AuthenticatedSongSerializer(all_songs, many=True)

        assert serializer.data[0]["UG_views"] == 1000000
        assert serializer.data[1]["UG_views"] == 2000000
        assert serializer.data[2]["UG_views"] == 3000000

    def test_serialize_song_UG_favourites_for_authenticated_user(self, all_songs):
        serializer = AuthenticatedSongSerializer(all_songs, many=True)

        assert serializer.data[0]["UG_favourites"] == 1000000
        assert serializer.data[1]["UG_favourites"] == 2000000
        assert serializer.data[2]["UG_favourites"] == 3000000

    def test_user_authenticated_can_get_list_of_songs_with_name(
        self,
        all_songs,
        logged_in_client,
    ):
        url = reverse("api:v1:songs-list")
        response = logged_in_client.get(url)

        assert response.status_code == 200, response.data
        assert response.json()[0]["name"] == "A Hard Day's Night"
        assert response.json()[1]["name"] == "I Should Have Known Better"
        assert response.json()[2]["name"] == "Can't Buy Me Love"

    def test_user_authenticated_can_get_list_of_songs_with_album(
        self,
        all_songs,
        logged_in_client,
    ):
        url = reverse("api:v1:songs-list")
        response = logged_in_client.get(url)

        assert response.status_code == 200, response.data
        assert response.json()[0]["album"] == "A Hard Day's Night"
        assert response.json()[1]["album"] == "Magical Mystery Tour"
        assert response.json()[2]["album"] == "A Hard Day's Night"

    def test_user_authenticated_can_get_list_of_songs_with_rank(
        self,
        all_songs,
        logged_in_client,
    ):
        url = reverse("api:v1:songs-list")
        response = logged_in_client.get(url)

        assert response.status_code == 200, response.data
        assert response.json()[0]["rank"] == 15
        assert response.json()[1]["rank"] == 20
        assert response.json()[2]["rank"] == 30

    def test_user_authenticated_can_get_list_of_songs_with_writer(
        self,
        all_songs,
        logged_in_client,
    ):
        url = reverse("api:v1:songs-list")
        response = logged_in_client.get(url)

        assert response.status_code == 200, response.data
        assert response.json()[0]["writer"] == "John Lennon\nPaul McCartney"
        assert response.json()[1]["writer"] == "Paul McCartney"
        assert response.json()[2]["writer"] == "John Lennon"

    def test_user_authenticated_can_get_list_of_songs_with_year_release(
        self,
        all_songs,
        logged_in_client,
    ):
        url = reverse("api:v1:songs-list")
        response = logged_in_client.get(url)

        assert response.status_code == 200, response.data
        assert response.json()[0]["year_release"] == 1964
        assert response.json()[1]["year_release"] == 1966
        assert response.json()[2]["year_release"] == 1966

    def test_user_authenticated_can_get_list_of_songs_with_singer(
        self,
        all_songs,
        logged_in_client,
    ):
        url = reverse("api:v1:songs-list")
        response = logged_in_client.get(url)

        assert response.status_code == 200, response.data
        assert response.json()[0]["singer"] == "John Lennon\n(with Paul McCartney)"
        assert response.json()[1]["singer"] == "Paul McCartne)"
        assert response.json()[2]["singer"] == "John Lennon"

    def test_user_authenticated_can_get_list_of_songs_with_song_time(
        self,
        all_songs,
        logged_in_client,
    ):
        url = reverse("api:v1:songs-list")
        response = logged_in_client.get(url)

        assert response.status_code == 200, response.data
        assert response.json()[0]["song_time"] == "02:32"
        assert response.json()[1]["song_time"] == "02:32"
        assert response.json()[2]["song_time"] == "02:32"

    def test_user_authenticated_can_get_list_of_songs_with_spotify_streams(
        self,
        all_songs,
        logged_in_client,
    ):
        url = reverse("api:v1:songs-list")
        response = logged_in_client.get(url)

        assert response.status_code == 200, response.data
        assert response.json()[0]["spotify_streams"] == "1,000,000"
        assert response.json()[1]["spotify_streams"] == "2,000,000"
        assert response.json()[2]["spotify_streams"] == "3,000,000"

    def test_user_authenticated_can_get_list_of_songs_with_rollling_stone_rank(
        self,
        all_songs,
        logged_in_client,
    ):
        url = reverse("api:v1:songs-list")
        response = logged_in_client.get(url)

        assert response.status_code == 200, response.data
        assert response.json()[0]["rolling_stone_rank"] == 1
        assert response.json()[1]["rolling_stone_rank"] == 2
        assert response.json()[2]["rolling_stone_rank"] == 3

    def test_user_authenticated_can_get_list_of_songs_with_NME_rank(
        self,
        all_songs,
        logged_in_client,
    ):
        url = reverse("api:v1:songs-list")
        response = logged_in_client.get(url)

        assert response.status_code == 200, response.data
        assert response.json()[0]["NME_rank"] == 1
        assert response.json()[1]["NME_rank"] == 2
        assert response.json()[2]["NME_rank"] == 3

    def test_user_authenticated_can_get_list_of_songs_with_UG_favourites(
        self,
        all_songs,
        logged_in_client,
    ):
        url = reverse("api:v1:songs-list")
        response = logged_in_client.get(url)

        assert response.status_code == 200, response.data
        assert response.json()[0]["UG_favourites"] == 1000000
        assert response.json()[1]["UG_favourites"] == 2000000
        assert response.json()[2]["UG_favourites"] == 3000000

    def test_user_authenticated_can_get_list_of_songs_with_UG_views(
        self,
        all_songs,
        logged_in_client,
    ):
        url = reverse("api:v1:songs-list")
        response = logged_in_client.get(url)

        assert response.status_code == 200, response.data
        assert response.json()[0]["UG_views"] == 1000000
        assert response.json()[1]["UG_views"] == 2000000
        assert response.json()[2]["UG_views"] == 3000000

    def test_user_authenticated_can_get_list_of_songs_with_UG_favourites(
        self,
        all_songs,
        logged_in_client,
    ):
        url = reverse("api:v1:songs-list")
        response = logged_in_client.get(url)

        assert response.status_code == 200, response.data
        assert response.json()[0]["UG_favourites"] == 1000000
        assert response.json()[1]["UG_favourites"] == 2000000
        assert response.json()[2]["UG_favourites"] == 3000000
