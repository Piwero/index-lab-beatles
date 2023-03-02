import csv

import pytest

from songs.services import ParseCSVDataHandler


@pytest.fixture
def beatles_songs():
    parser = ParseCSVDataHandler("songs/tests/data_sample.csv")
    return parser.parse()


class TestImportCSVDataToDB:
    class TestParseData:
        def test_song_name(self, beatles_songs):
            assert beatles_songs[0]["Song Name"] == "A Hard Day's Night"
            assert beatles_songs[1]["Song Name"] == "All You Need Is Love"
            assert beatles_songs[2]["Song Name"] == "Can't Buy Me Love"

        def test_rank(self, beatles_songs):
            assert beatles_songs[0]["Rank"] == "15"
            assert beatles_songs[1]["Rank"] == "4"
            assert beatles_songs[2]["Rank"] == "14"

        def test_album(self, beatles_songs):
            assert beatles_songs[0]["Album"] == "A Hard Day's Night"
            assert beatles_songs[1]["Album"] == "Magical Mystery Tour"
            assert beatles_songs[2]["Album"] == "A Hard Day's Night"

        def test_song_writer(self, beatles_songs):
            assert beatles_songs[0]["Song Writer"] == "John Lennon\nPaul McCartney"
            assert beatles_songs[1]["Song Writer"] == "John Lennon\nPaul McCartney"
            assert beatles_songs[2]["Song Writer"] == "John Lennon\nPaul McCartney"

        def test_singer(self, beatles_songs):
            assert beatles_songs[0]["Singer"] == "John Lennon\n(with Paul McCartney)"
            assert beatles_songs[1]["Singer"] == "John Lennon"
            assert beatles_songs[2]["Singer"] == "Paul McCartney"

        def test_year_released(self, beatles_songs):
            assert beatles_songs[0]["Year Released"] == "1964"
            assert beatles_songs[1]["Year Released"] == "1967"
            assert beatles_songs[2]["Year Released"] == "1964"

        def test_song_time(self, beatles_songs):
            assert beatles_songs[0]["Song Time"] == "02:32"
            assert beatles_songs[1]["Song Time"] == "03:47"
            assert beatles_songs[2]["Song Time"] == "02:11"

        def test_spotify_streams(self, beatles_songs):
            assert beatles_songs[0]["Spotify Streams"] == "154,811,402"
            assert beatles_songs[1]["Spotify Streams"] == "146,809,784"
            assert beatles_songs[2]["Spotify Streams"] == "110,537,137"

        def test_rolling_stone_rank(self, beatles_songs):
            assert (
                beatles_songs[0]["Rolling Stone 100 Greatest Beatles Songs Ranking"]
                == "11"
            )
            assert (
                beatles_songs[1]["Rolling Stone 100 Greatest Beatles Songs Ranking"]
                == "21"
            )
            assert (
                beatles_songs[2]["Rolling Stone 100 Greatest Beatles Songs Ranking"]
                == "29"
            )

        def test_nme_rank(self, beatles_songs):
            assert beatles_songs[0]["NME Top 50 Beatles Songs Ranking"] == "19"
            assert beatles_songs[1]["NME Top 50 Beatles Songs Ranking"] == ""
            assert beatles_songs[2]["NME Top 50 Beatles Songs Ranking"] == "43"

        def test_ug_views(self, beatles_songs):
            assert beatles_songs[0]["UG Views"] == "1031725"
            assert beatles_songs[1]["UG Views"] == "1081533"
            assert beatles_songs[2]["UG Views"] == "1069188"

        def test_ug_favourites(self, beatles_songs):
            assert beatles_songs[0]["UG Favourites"] == "23699"
            assert beatles_songs[1]["UG Favourites"] == "53208"
            assert beatles_songs[2]["UG Favourites"] == "27060"

    class TestImportDataToDB:
        def test_create_song_with_name_from_parsed_data(self, db, beatles_songs):
            parser = ParseCSVDataHandler("songs/tests/data_sample.csv")
            parsed_data = parser.parse()
            songs = parser.create_songs_from_parsed_data(parsed_data)

            assert getattr(songs[0], "name") == "A Hard Day's Night"

        def test_create_song_with_rank_from_parsed_data(self, db, beatles_songs):
            parser = ParseCSVDataHandler("songs/tests/data_sample.csv")
            parsed_data = parser.parse()
            songs = parser.create_songs_from_parsed_data(parsed_data)

            assert getattr(songs[0], "rank") == 15

        def test_create_song_with_album_from_parsed_data(self, db, beatles_songs):
            parser = ParseCSVDataHandler("songs/tests/data_sample.csv")
            parsed_data = parser.parse()
            songs = parser.create_songs_from_parsed_data(parsed_data)

            assert getattr(songs[0], "album") == "A Hard Day's Night"

        def test_create_song_with_writer_from_parsed_data(self, db, beatles_songs):
            parser = ParseCSVDataHandler("songs/tests/data_sample.csv")
            parsed_data = parser.parse()
            songs = parser.create_songs_from_parsed_data(parsed_data)

            assert getattr(songs[0], "writer") == "John Lennon\nPaul McCartney"

        def test_create_song_with_singer_from_parsed_data(self, db, beatles_songs):
            parser = ParseCSVDataHandler("songs/tests/data_sample.csv")
            parsed_data = parser.parse()
            songs = parser.create_songs_from_parsed_data(parsed_data)

            assert getattr(songs[0], "singer") == "John Lennon\n(with Paul McCartney)"

        def test_create_song_with_year_release_from_parsed_data(
            self, db, beatles_songs
        ):
            parser = ParseCSVDataHandler("songs/tests/data_sample.csv")
            parsed_data = parser.parse()
            songs = parser.create_songs_from_parsed_data(parsed_data)

            assert getattr(songs[0], "year_release") == 1964

        def test_create_song_with_song_time_from_parsed_data(self, db, beatles_songs):
            parser = ParseCSVDataHandler("songs/tests/data_sample.csv")
            parsed_data = parser.parse()
            songs = parser.create_songs_from_parsed_data(parsed_data)

            assert getattr(songs[0], "song_time") == "02:32"

        def test_create_song_with_spotify_streams_from_parsed_data(
            self, db, beatles_songs
        ):
            parser = ParseCSVDataHandler("songs/tests/data_sample.csv")
            parsed_data = parser.parse()
            songs = parser.create_songs_from_parsed_data(parsed_data)

            assert getattr(songs[0], "spotify_streams") == "154,811,402"

        def test_create_song_with_rolling_stone_rank_from_parsed_data(
            self, db, beatles_songs
        ):
            parser = ParseCSVDataHandler("songs/tests/data_sample.csv")
            parsed_data = parser.parse()
            songs = parser.create_songs_from_parsed_data(parsed_data)

            assert getattr(songs[0], "rolling_stone_rank") == 11

        def test_create_song_with_nme_rank_from_parsed_data(self, db, beatles_songs):
            parser = ParseCSVDataHandler("songs/tests/data_sample.csv")
            parsed_data = parser.parse()
            songs = parser.create_songs_from_parsed_data(parsed_data)

            assert getattr(songs[0], "NME_rank") == 19

        def test_create_song_with_ug_views_from_parsed_data(self, db, beatles_songs):
            parser = ParseCSVDataHandler("songs/tests/data_sample.csv")
            parsed_data = parser.parse()
            songs = parser.create_songs_from_parsed_data(parsed_data)

            assert getattr(songs[0], "UG_views") == 1031725

        def test_create_song_with_ug_favourites_from_parsed_data(
            self, db, beatles_songs
        ):
            parser = ParseCSVDataHandler("songs/tests/data_sample.csv")
            parsed_data = parser.parse()
            songs = parser.create_songs_from_parsed_data(parsed_data)

            assert getattr(songs[0], "UG_favourites") == 23699
